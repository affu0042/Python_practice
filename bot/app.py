import cv2
import numpy as np
import math

# Constants
FRAME_WIDTH = 800
FRAME_HEIGHT = 600
BOT_RADIUS = 12
STEP = 10

# Wall Positions (Fixed)
wall_A = (FRAME_WIDTH // 2, 60)
wall_B = (100, FRAME_HEIGHT - 100)
wall_C = (FRAME_WIDTH - 100, FRAME_HEIGHT - 100)

# Bot State
bot_position = [FRAME_WIDTH // 2, FRAME_HEIGHT // 2]
bot_heading_angle = 0  # degrees
target_angle = 0       # degrees
trail_points = []

# Mouse state
mouse_dragging = False

# Helper: Distance between two points
def calculate_distance(p1, p2):
    return int(math.hypot(p1[0] - p2[0], p1[1] - p2[1]))

# Normalize angle between 0–360
def normalize_angle(angle):
    return angle % 360

# Smooth rotation
def update_heading():
    global bot_heading_angle
    diff = (target_angle - bot_heading_angle + 360) % 360
    if diff > 180:
        diff -= 360
    bot_heading_angle += diff * 0.15  # smoothness factor
    bot_heading_angle = normalize_angle(bot_heading_angle)

# Draw background grid
def draw_grid(frame, spacing=40):
    for x in range(0, FRAME_WIDTH, spacing):
        cv2.line(frame, (x, 0), (x, FRAME_HEIGHT), (230, 230, 230), 1)
    for y in range(0, FRAME_HEIGHT, spacing):
        cv2.line(frame, (0, y), (FRAME_WIDTH, y), (230, 230, 230), 1)

# Draw compass (top-right corner)
def draw_compass(frame, center, angle):
    r = 35
    cv2.circle(frame, center, r, (100, 100, 100), 2)

    directions = ['N', 'E', 'S', 'W']
    for i, d in enumerate(directions):
        a = math.radians(i * 90)
        tx = int(center[0] + (r + 10) * math.cos(a))
        ty = int(center[1] + (r + 10) * math.sin(a))
        cv2.putText(frame, d, (tx - 10, ty + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120, 120, 120), 2)

    # Draw heading arrow
    angle_rad = math.radians(angle)
    end_x = int(center[0] + r * math.cos(angle_rad))
    end_y = int(center[1] + r * math.sin(angle_rad))
    cv2.arrowedLine(frame, center, (end_x, end_y), (0, 0, 0), 2, tipLength=0.4)

    # Degree label (moved lower to prevent overlap)
    cv2.putText(frame, f"{angle:.1f}°", (center[0] - 25, center[1] + 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (80, 80, 80), 2)

# Draw all elements
def draw_interface():
    frame = np.ones((FRAME_HEIGHT, FRAME_WIDTH, 3), dtype=np.uint8) * 255
    draw_grid(frame)

    # Trail with gradient color
    for i in range(1, len(trail_points)):
        fade = int(255 * i / len(trail_points))
        color = (180, 180, 255 - fade)
        cv2.line(frame, trail_points[i - 1], trail_points[i], color, 2)

    # Walls
    for wall, label, color in zip([wall_A, wall_B, wall_C], ['A', 'B', 'C'],
                                  [(0, 0, 255), (0, 200, 0), (255, 80, 80)]):
        cv2.circle(frame, wall, 10, color, -1)
        cv2.putText(frame, f"{label} ({wall[0]}, {wall[1]})", (wall[0] - 50, wall[1] - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Bot
    angle_rad = math.radians(bot_heading_angle)
    head_x = int(bot_position[0] + BOT_RADIUS * 2 * math.cos(angle_rad))
    head_y = int(bot_position[1] + BOT_RADIUS * 2 * math.sin(angle_rad))
    cv2.circle(frame, tuple(bot_position), BOT_RADIUS, (0, 0, 0), -1)
    cv2.arrowedLine(frame, tuple(bot_position), (head_x, head_y), (0, 0, 0), 2, tipLength=0.4)

    # Compass (top-right corner)
    draw_compass(frame, (FRAME_WIDTH - 70, 70), bot_heading_angle)

    # Bot label
    cv2.putText(frame, f"Bot ({bot_position[0]}, {bot_position[1]})", (bot_position[0] - 50, bot_position[1] - 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (80, 80, 80), 2)

    # Distance Panel
    panel_y = 20
    for wall, label, color in zip([wall_A, wall_B, wall_C], ['A', 'B', 'C'],
                                  [(0, 0, 255), (0, 200, 0), (255, 80, 80)]):
        dist = calculate_distance(bot_position, wall)
        cv2.line(frame, tuple(bot_position), wall, color, 1)
        mid_x = (bot_position[0] + wall[0]) // 2
        mid_y = (bot_position[1] + wall[1]) // 2
        cv2.putText(frame, f"{label}:{dist}px", (mid_x, mid_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        cv2.putText(frame, f"Distance to {label}: {dist}px", (10, panel_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        panel_y += 25

    # Controls
    cv2.putText(frame, "W/A/S/D = Move   |   Mouse Drag = Aim + Jump   |   ESC = Quit",
                (10, FRAME_HEIGHT - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (80, 80, 80), 2)

    return frame

# Bot movement
def move_bot(key):
    global target_angle
    dx, dy = 0, 0
    if key == ord('w'):
        dy = -STEP
    elif key == ord('s'):
        dy = STEP
    elif key == ord('a'):
        dx = -STEP
    elif key == ord('d'):
        dx = STEP

    if dx or dy:
        bot_position[0] = min(max(bot_position[0] + dx, BOT_RADIUS), FRAME_WIDTH - BOT_RADIUS)
        bot_position[1] = min(max(bot_position[1] + dy, BOT_RADIUS), FRAME_HEIGHT - BOT_RADIUS)
        target_angle = normalize_angle(math.degrees(math.atan2(dy, dx)))

# Mouse click & drag
def click_event(event, x, y, flags, param):
    global mouse_dragging, target_angle
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_dragging = True
    elif event == cv2.EVENT_MOUSEMOVE and mouse_dragging:
        dx = x - bot_position[0]
        dy = y - bot_position[1]
        if dx or dy:
            target_angle = normalize_angle(math.degrees(math.atan2(dy, dx)))
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_dragging = False
        bot_position[0] = x
        bot_position[1] = y

# Init Window
cv2.namedWindow("Attractive Bot Simulation")
cv2.setMouseCallback("Attractive Bot Simulation", click_event)

# Main Loop
while True:
    update_heading()
    trail_points.append(tuple(bot_position))
    if len(trail_points) > 80:
        trail_points.pop(0)

    frame = draw_interface()
    cv2.imshow("Attractive Bot Simulation", frame)

    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break
    move_bot(key)

cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import math

# # Constants
# FRAME_WIDTH = 800
# FRAME_HEIGHT = 600
# BOT_RADIUS = 12
# STEP = 10

# # Walls
# wall_A = (FRAME_WIDTH // 2, 60)
# wall_B = (100, FRAME_HEIGHT - 100)
# wall_C = (FRAME_WIDTH - 100, FRAME_HEIGHT - 100)

# # Bot state
# bot_position = [FRAME_WIDTH // 2, FRAME_HEIGHT // 2]
# bot_heading_angle = 0  # degrees
# target_angle = 0       # For smooth transitions
# trail_points = []

# # Mouse tracking
# mouse_dragging = False
# drag_start = None

# # Distance calculation
# def calculate_distance(p1, p2):
#     return int(math.hypot(p1[0] - p2[0], p1[1] - p2[1]))

# # Draw grid
# def draw_grid(img, spacing=40):
#     for x in range(0, img.shape[1], spacing):
#         cv2.line(img, (x, 0), (x, img.shape[0]), (220, 220, 220), 1)
#     for y in range(0, img.shape[0], spacing):
#         cv2.line(img, (0, y), (img.shape[1], y), (220, 220, 220), 1)

# # Normalize angle between 0–360
# def normalize_angle(angle):
#     return angle % 360

# # Smooth angle transition
# def update_heading():
#     global bot_heading_angle
#     diff = (target_angle - bot_heading_angle + 360) % 360
#     if diff > 180:
#         diff -= 360
#     bot_heading_angle += diff * 0.1
#     bot_heading_angle = normalize_angle(bot_heading_angle)

# # Draw compass around the bot
# def draw_compass(frame, center, angle):
#     r = 30
#     angle_rad = math.radians(angle)
#     end_x = int(center[0] + r * math.cos(angle_rad))
#     end_y = int(center[1] + r * math.sin(angle_rad))
#     cv2.circle(frame, center, r, (100, 100, 100), 1)
#     cv2.line(frame, center, (end_x, end_y), (0, 0, 0), 2)
#     cv2.putText(frame, f"{angle:.1f}°", (center[0] - 20, center[1] + 45),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (80, 80, 80), 2)

# # Draw interface
# def draw_interface():
#     frame = np.ones((FRAME_HEIGHT, FRAME_WIDTH, 3), dtype=np.uint8) * 255
#     draw_grid(frame)

#     # Trail
#     for i in range(1, len(trail_points)):
#         cv2.line(frame, trail_points[i - 1], trail_points[i], (180, 180, 180), 2)

#     # Walls
#     for wall, label, color in zip([wall_A, wall_B, wall_C], ['A', 'B', 'C'], [(0, 0, 255), (0, 255, 0), (255, 0, 0)]):
#         cv2.circle(frame, wall, 10, color, -1)
#         cv2.putText(frame, f"{label} ({wall[0]}, {wall[1]})", (wall[0] - 50, wall[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#     # Bot and heading
#     angle_rad = math.radians(bot_heading_angle)
#     head_x = int(bot_position[0] + BOT_RADIUS * 2 * math.cos(angle_rad))
#     head_y = int(bot_position[1] + BOT_RADIUS * 2 * math.sin(angle_rad))
#     cv2.circle(frame, tuple(bot_position), BOT_RADIUS, (0, 0, 0), -1)
#     cv2.arrowedLine(frame, tuple(bot_position), (head_x, head_y), (0, 0, 0), 2, tipLength=0.4)

#     # Compass
#     draw_compass(frame, (bot_position[0], bot_position[1] - 60), bot_heading_angle)

#     # Label
#     cv2.putText(frame, f"Bot ({bot_position[0]}, {bot_position[1]})", (bot_position[0] - 40, bot_position[1] - 25),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (80, 80, 80), 2)

#     # Distance lines & labels
#     panel_y = 20
#     for wall, label, color in zip([wall_A, wall_B, wall_C], ['A', 'B', 'C'], [(0, 0, 255), (0, 255, 0), (255, 0, 0)]):
#         dist = calculate_distance(bot_position, wall)
#         cv2.line(frame, tuple(bot_position), wall, color, 1)
#         mid_x = (bot_position[0] + wall[0]) // 2
#         mid_y = (bot_position[1] + wall[1]) // 2
#         cv2.putText(frame, f"{label}:{dist}px", (mid_x, mid_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
#         cv2.putText(frame, f"Distance to {label}: {dist}px", (10, panel_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
#         panel_y += 25

#     # Controls
#     cv2.putText(frame, "W/A/S/D: Move | Click & Drag: Aim & Jump | ESC: Quit", (10, FRAME_HEIGHT - 10),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 100), 2)
#     return frame

# # Movement and direction update
# def move_bot(key):
#     global target_angle
#     dx, dy = 0, 0
#     if key == ord('w'):
#         dy = -STEP
#     elif key == ord('s'):
#         dy = STEP
#     elif key == ord('a'):
#         dx = -STEP
#     elif key == ord('d'):
#         dx = STEP

#     if dx or dy:
#         bot_position[0] = min(max(bot_position[0] + dx, BOT_RADIUS), FRAME_WIDTH - BOT_RADIUS)
#         bot_position[1] = min(max(bot_position[1] + dy, BOT_RADIUS), FRAME_HEIGHT - BOT_RADIUS)
#         target_angle = normalize_angle(math.degrees(math.atan2(dy, dx)))

# # Mouse drag logic
# def click_event(event, x, y, flags, param):
#     global mouse_dragging, target_angle, bot_position
#     if event == cv2.EVENT_LBUTTONDOWN:
#         mouse_dragging = True
#     elif event == cv2.EVENT_MOUSEMOVE and mouse_dragging:
#         dx = x - bot_position[0]
#         dy = y - bot_position[1]
#         if dx != 0 or dy != 0:
#             target_angle = normalize_angle(math.degrees(math.atan2(dy, dx)))
#     elif event == cv2.EVENT_LBUTTONUP:
#         mouse_dragging = False
#         bot_position[0] = x
#         bot_position[1] = y

# # Setup
# cv2.namedWindow("Advanced Bot Simulation")
# cv2.setMouseCallback("Advanced Bot Simulation", click_event)

# # Main loop
# while True:
#     update_heading()
#     trail_points.append(tuple(bot_position))
#     if len(trail_points) > 100:
#         trail_points.pop(0)

#     frame = draw_interface()
#     cv2.imshow("Advanced Bot Simulation", frame)

#     key = cv2.waitKey(30) & 0xFF
#     if key == 27:
#         break
#     move_bot(key)

# cv2.destroyAllWindows()



# import cv2
# import numpy as np
# import math

# # Constants
# FRAME_WIDTH = 800
# FRAME_HEIGHT = 600
# BOT_RADIUS = 12
# STEP = 10

# # Wall Positions (Fixed)
# wall_A = (FRAME_WIDTH // 2, 60)
# wall_B = (100, FRAME_HEIGHT - 100)
# wall_C = (FRAME_WIDTH - 100, FRAME_HEIGHT - 100)

# # Movable Bot
# bot_position = [FRAME_WIDTH // 2, FRAME_HEIGHT // 2]
# trail_points = []  # to store bot path

# # Distance calculation
# def calculate_distance(p1, p2):
#     return int(math.hypot(p1[0] - p2[0], p1[1] - p2[1]))

# # Draw background grid
# def draw_grid(img, spacing=40):
#     for x in range(0, img.shape[1], spacing):
#         cv2.line(img, (x, 0), (x, img.shape[0]), (220, 220, 220), 1)
#     for y in range(0, img.shape[0], spacing):
#         cv2.line(img, (0, y), (img.shape[1], y), (220, 220, 220), 1)

# # Draw everything
# def draw_interface():
#     frame = np.ones((FRAME_HEIGHT, FRAME_WIDTH, 3), dtype=np.uint8) * 255
#     draw_grid(frame)

#     # Trail
#     for i in range(1, len(trail_points)):
#         cv2.line(frame, trail_points[i - 1], trail_points[i], (180, 180, 180), 2)

#     # Draw walls
#     for wall, label, color in zip([wall_A, wall_B, wall_C], ['A', 'B', 'C'], [(0, 0, 255), (0, 255, 0), (255, 0, 0)]):
#         cv2.circle(frame, wall, 10, color, -1)
#         cv2.putText(frame, f"{label} ({wall[0]}, {wall[1]})", (wall[0] - 50, wall[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#     # Draw Bot
#     cv2.circle(frame, tuple(bot_position), BOT_RADIUS, (0, 0, 0), -1)
#     cv2.putText(frame, f"Bot ({bot_position[0]}, {bot_position[1]})", (bot_position[0] - 40, bot_position[1] - 20),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (80, 80, 80), 2)

#     # Draw lines and distances
#     panel_y = 20
#     for wall, label, color in zip([wall_A, wall_B, wall_C], ['A', 'B', 'C'], [(0, 0, 255), (0, 255, 0), (255, 0, 0)]):
#         dist = calculate_distance(bot_position, wall)
#         cv2.line(frame, tuple(bot_position), wall, color, 1)

#         # Midpoint label
#         mid_x = (bot_position[0] + wall[0]) // 2
#         mid_y = (bot_position[1] + wall[1]) // 2
#         cv2.putText(frame, f"{label}:{dist}px", (mid_x, mid_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

#         # Telemetry Panel
#         cv2.putText(frame, f"Distance to {label}: {dist}px", (10, panel_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
#         panel_y += 25

#     # Controls
#     cv2.putText(frame, "W/A/S/D: Move | Click: Jump | ESC: Quit", (10, FRAME_HEIGHT - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 100), 2)

#     return frame

# # Bot movement
# def move_bot(key):
#     if key == ord('w'):
#         bot_position[1] = max(bot_position[1] - STEP, BOT_RADIUS)
#     elif key == ord('s'):
#         bot_position[1] = min(bot_position[1] + STEP, FRAME_HEIGHT - BOT_RADIUS)
#     elif key == ord('a'):
#         bot_position[0] = max(bot_position[0] - STEP, BOT_RADIUS)
#     elif key == ord('d'):
#         bot_position[0] = min(bot_position[0] + STEP, FRAME_WIDTH - BOT_RADIUS)

# # Mouse event to click and move bot instantly
# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         bot_position[0] = x
#         bot_position[1] = y

# # Main loop
# cv2.namedWindow("Advanced Bot Simulation")
# cv2.setMouseCallback("Advanced Bot Simulation", click_event)

# while True:
#     trail_points.append(tuple(bot_position))
#     if len(trail_points) > 100:
#         trail_points.pop(0)

#     frame = draw_interface()
#     cv2.imshow("Advanced Bot Simulation", frame)

#     key = cv2.waitKey(100) & 0xFF
#     if key == 27:
#         break
#     move_bot(key)

# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# import math

# # Constants
# FRAME_WIDTH = 640
# FRAME_HEIGHT = 480
# BOT_RADIUS = 12
# STEP = 10

# # Wall Positions (Fixed)
# wall_A = (320, 50)
# wall_B = (100, 400)
# wall_C = (540, 400)

# # Movable Bot Initial Position (Center)
# bot_position = [320, 240]

# def calculate_distance(p1, p2):
#     """Calculate Euclidean distance between two points."""
#     return int(math.hypot(p1[0] - p2[0], p1[1] - p2[1]))

# def draw_interface():
#     """Draw the simulation frame with walls, bot, and distance lines."""
#     frame = np.ones((FRAME_HEIGHT, FRAME_WIDTH, 3), dtype=np.uint8) * 255

#     # Draw Walls
#     for wall, label, color in zip([wall_A, wall_B, wall_C], ['A', 'B', 'C'], [(0, 0, 255), (0, 255, 0), (255, 0, 0)]):
#         cv2.circle(frame, wall, 10, color, -1)
#         cv2.putText(frame, label, (wall[0] - 15, wall[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

#     # Draw Bot
#     cv2.circle(frame, tuple(bot_position), BOT_RADIUS, (0, 0, 0), -1)
#     cv2.putText(frame, "Bot", (bot_position[0] - 20, bot_position[1] - 20),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 50, 50), 2)

#     # Draw lines and distances
#     for wall, label, color in zip([wall_A, wall_B, wall_C], ['A', 'B', 'C'], [(0, 0, 255), (0, 255, 0), (255, 0, 0)]):
#         dist = calculate_distance(bot_position, wall)
#         cv2.line(frame, tuple(bot_position), wall, color, 1)
#         mid_x = (bot_position[0] + wall[0]) // 2
#         mid_y = (bot_position[1] + wall[1]) // 2
#         cv2.putText(frame, f"{label}: {dist}px", (mid_x, mid_y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

#     # Instructions
#     instructions = "Move Bot: W/A/S/D | Quit: ESC"
#     cv2.putText(frame, instructions, (10, FRAME_HEIGHT - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 100), 2)

#     return frame

# def move_bot(key):
#     """Update bot's position based on key pressed."""
#     if key == ord('w'):  # UP
#         bot_position[1] = max(bot_position[1] - STEP, BOT_RADIUS)
#     elif key == ord('s'):  # DOWN
#         bot_position[1] = min(bot_position[1] + STEP, FRAME_HEIGHT - BOT_RADIUS)
#     elif key == ord('a'):  # LEFT
#         bot_position[0] = max(bot_position[0] - STEP, BOT_RADIUS)
#     elif key == ord('d'):  # RIGHT
#         bot_position[0] = min(bot_position[0] + STEP, FRAME_WIDTH - BOT_RADIUS)

# # Main Loop
# cv2.namedWindow("Bot Distance Simulation")

# while True:
#     frame = draw_interface()
#     cv2.imshow("Bot Distance Simulation", frame)

#     key = cv2.waitKey(100) & 0xFF
#     if key == 27:  # ESC to quit
#         break

#     move_bot(key)

# cv2.destroyAllWindows()
