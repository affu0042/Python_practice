# ==========================
# IMPORT LIBRARIES
# ==========================
import cv2                      # OpenCV library (for image editing and webcam)
import numpy as np              # NumPy library (for array/matrix operations)
import tkinter as tk            # Tkinter (to create a GUI window with buttons)
from tkinter import filedialog, messagebox, simpledialog
# filedialog = open/save file boxes
# messagebox = pop-up messages
# simpledialog = pop-up for entering text

from PIL import Image, ImageTk  # Pillow library (for converting images to display in Tkinter)

# ==========================
# CLASS: PhotoEditor
# This part builds the GUI photo editor
# ==========================
class PhotoEditor:
    def __init__(self, root):
        # Save the main window
        self.root = root
        self.root.title("Class 8 Photo Editor")   # Window title

        # Initialize variables to store images
        self.original_image = None   # Image after opening
        self.current_image = None    # Image after editing
        self.history = []            # To keep track of versions (for undo)
        self.current_state = -1      # Index of current version in history

        # Create all the buttons and canvas
        self.create_widgets()

    # ==========================
    # Create buttons and a canvas to show the image
    # ==========================
    def create_widgets(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, padx=5, pady=5)  # Place buttons on top

        # Each button performs an action
        tk.Button(button_frame, text="Open Image", command=self.open_image).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Grayscale", command=self.apply_grayscale).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Rotate 90°", command=self.rotate_image).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Flip Horizontal", command=self.flip_image).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Crop", command=self.start_crop).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Add Text", command=self.add_text).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Undo", command=self.undo).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Save", command=self.save_image).pack(side=tk.LEFT)

        # Canvas is like a blank board where we display the image
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

    # ==========================
    # Open an image using file dialog
    # ==========================
    def open_image(self):
        path = filedialog.askopenfilename()  # Ask user to select a file
        if path:
            self.original_image = cv2.imread(path)       # Read image using OpenCV
            self.current_image = self.original_image.copy()
            self.history = [self.current_image.copy()]   # Save first version
            self.current_state = 0
            self.show_image()                            # Display the image

    # ==========================
    # Show image on the Tkinter canvas
    # ==========================
    def show_image(self):
        if self.current_image is not None:
            # Convert image from BGR (OpenCV) to RGB (Tkinter)
            img_rgb = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)           # Convert to Pillow image
            img_tk = ImageTk.PhotoImage(img_pil)         # Convert to Tkinter-compatible image

            # Resize the canvas and display the image
            self.canvas.config(width=img_tk.width(), height=img_tk.height())
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.canvas.image = img_tk                   # Save reference

    # ==========================
    # Save a new version in history and show it
    # ==========================
    def update_history(self, new_image):
        # Remove redo history if we are in middle
        if self.current_state < len(self.history) - 1:
            self.history = self.history[:self.current_state + 1]

        # Add new image
        self.history.append(new_image.copy())
        self.current_state += 1
        self.current_image = new_image
        self.show_image()

    # ==========================
    # Convert to grayscale
    # ==========================
    def apply_grayscale(self):
        if self.check_image():
            gray = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
            new_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # Convert back to BGR so everything stays same
            self.update_history(new_image)

    # ==========================
    # Rotate image 90 degrees clockwise
    # ==========================
    def rotate_image(self):
        if self.check_image():
            new_image = cv2.rotate(self.current_image, cv2.ROTATE_90_CLOCKWISE)
            self.update_history(new_image)

    # ==========================
    # Flip image horizontally (mirror)
    # ==========================
    def flip_image(self):
        if self.check_image():
            new_image = cv2.flip(self.current_image, 1)
            self.update_history(new_image)

    # ==========================
    # Crop: select an area with mouse in a separate OpenCV window
    # ==========================
    def start_crop(self):
        if self.check_image():
            messagebox.showinfo("Crop", "Drag mouse to select area and press ENTER")
            winname = "Select Crop Area"
            cv2.imshow(winname, self.current_image)
            roi = cv2.selectROI(winname, self.current_image, fromCenter=False, showCrosshair=True)
            cv2.destroyWindow(winname)

            if roi and all(i > 0 for i in roi[2:]):
                x, y, w, h = roi
                new_image = self.current_image[y:y + h, x:x + w].copy()
                self.update_history(new_image)
            else:
                messagebox.showinfo("Info", "No area selected to crop.")

    # ==========================
    # Add text: ask for text and draw it on image
    # ==========================
    def add_text(self):
        if self.check_image():
            text = simpledialog.askstring("Text", "Enter text:")  # Pop-up input
            if text:
                new_image = self.current_image.copy()
                cv2.putText(new_image, text, (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                self.update_history(new_image)

    # ==========================
    # Undo: go back one step
    # ==========================
    def undo(self):
        if self.current_state > 0:
            self.current_state -= 1
            self.current_image = self.history[self.current_state].copy()
            self.show_image()

    # ==========================
    # Save image to a file
    # ==========================
    def save_image(self):
        if self.check_image():
            path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if path:
                cv2.imwrite(path, self.current_image)

    # ==========================
    # Check if image is loaded
    # ==========================
    def check_image(self):
        if self.current_image is None:
            messagebox.showerror("Error", "Open an image first!")
            return False
        return True

# ==========================
# FUNCTION: interactive_editor
# This part opens webcam and allows live editing
# ==========================
def interactive_editor():
    cap = cv2.VideoCapture(0)                      # Start webcam
    cv2.namedWindow("Interactive Image Editor")    # Create a window

    # Callback for trackbars
    def nothing(x): pass

    # Create trackbars (sliders) for editing
    cv2.createTrackbar("Brightness", "Interactive Image Editor", 50, 100, nothing)
    cv2.createTrackbar("Contrast", "Interactive Image Editor", 50, 100, nothing)
    cv2.createTrackbar("Filter", "Interactive Image Editor", 0, 5, nothing)  # 0:none, 1:gray, 2:blur, 3:edges, 4:sketch, 5:invert
    cv2.createTrackbar("Rotation", "Interactive Image Editor", 0, 360, nothing)
    cv2.createTrackbar("Flip", "Interactive Image Editor", 0, 2, nothing)    # 0:none,1:horizontal,2:vertical

    # Drawing variables
    drawing = False
    ix, iy = -1, -1
    color = (0, 255, 0)
    thickness = 2

    # Function to draw with mouse
    def draw(event, x, y, flags, param):
        nonlocal ix, iy, drawing, img
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                cv2.line(img, (ix, iy), (x, y), color, thickness)
                ix, iy = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.line(img, (ix, iy), (x, y), color, thickness)

    cv2.setMouseCallback("Interactive Image Editor", draw)  # Attach mouse callback

    while True:
        ret, img = cap.read()    # Read frame from webcam
        if not ret:
            break

        # Get slider values
        brightness = cv2.getTrackbarPos("Brightness", "Interactive Image Editor") - 50
        contrast = cv2.getTrackbarPos("Contrast", "Interactive Image Editor") / 50
        filter_mode = cv2.getTrackbarPos("Filter", "Interactive Image Editor")
        rotation = cv2.getTrackbarPos("Rotation", "Interactive Image Editor")
        flip_mode = cv2.getTrackbarPos("Flip", "Interactive Image Editor")

        # Adjust brightness and contrast
        img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)

        # Apply filters
        if filter_mode == 1:  # Grayscale
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif filter_mode == 2:  # Blur
            img = cv2.GaussianBlur(img, (15, 15), 0)
        elif filter_mode == 3:  # Edge detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        elif filter_mode == 4:  # Sketch effect
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            inverted = cv2.bitwise_not(gray)
            blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
            sketch = cv2.divide(gray, blurred, scale=256.0)
            img = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
        elif filter_mode == 5:  # Invert colors
            img = cv2.bitwise_not(img)

        # Rotate the image
        if rotation != 0:
            h, w = img.shape[:2]
            M = cv2.getRotationMatrix2D((w // 2, h // 2), rotation, 1.0)
            img = cv2.warpAffine(img, M, (w, h))

        # Flip image
        if flip_mode == 1:
            img = cv2.flip(img, 1)
        elif flip_mode == 2:
            img = cv2.flip(img, 0)

        # Add text on the webcam video
        cv2.putText(img, "OpenCV Mini Project", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        cv2.imshow("Interactive Image Editor", img)  # Show the frame
        if cv2.waitKey(1) == 27:  # Exit when ESC key is pressed
            break

    cap.release()
    cv2.destroyAllWindows()

# ==========================
# MAIN PROGRAM START
# ==========================
if __name__ == "__main__":
    print("Choose Mode:")
    print("1. Photo Editor (Tkinter GUI)")
    print("2. Interactive Editor (Webcam OpenCV)")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        root = tk.Tk()
        app = PhotoEditor(root)
        root.mainloop()
    elif choice == "2":
        interactive_editor()
    else:
        print("Invalid choice!")
