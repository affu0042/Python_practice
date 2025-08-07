import cv2
import numpy as np

def edit_for_birthday_card(input_path, output_path, card_width=1000, card_height=700):
    # 1. Load image
    img = cv2.imread(input_path)
    if img is None:
        print("Error: Could not load image")
        return

    # 2. Resize image to fit within card dimensions (maintaining aspect ratio)
    h, w = img.shape[:2]
    scale = min(card_width / w, card_height / h)
    resized = cv2.resize(img, (int(w * scale), int(h * scale)))

    # 3. Detect face or manually select ROI
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        # Use largest detected face
        faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)
        x, y, w, h = faces[0]
        print("Auto-detected face - adjust if needed")
    else:
        # Manual selection if no face detected
        print("No face auto-detected - please select person manually")
        r = cv2.selectROI("Select the person (press Enter to confirm)", resized)
        x, y, w, h = r
        cv2.destroyAllWindows()

    # 4. Add padding (40%) around the region
    padding_w = int(w * 0.4)
    padding_h = int(h * 0.4)
    x1 = max(0, x - padding_w)
    y1 = max(0, y - padding_h)
    x2 = min(resized.shape[1], x + w + padding_w)
    y2 = min(resized.shape[0], y + h + padding_h)

    # 5. Crop the image
    cropped = resized[y1:y2, x1:x2]

    # 6. Resize cropped image to exact card dimensions
    final = cv2.resize(cropped, (card_width, card_height))

    # 7. Add a decorative border
    final = cv2.copyMakeBorder(final, 10, 10, 10, 10,
                               cv2.BORDER_CONSTANT, value=[255, 200, 200])

    # 8. Save and display
    cv2.imwrite(output_path, final)
    print(f"Birthday card image saved to {output_path}")
    cv2.imshow("Birthday Card", final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_photo = r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\pexels-askar-abayev-5638706.jpg"  # Replace with your image path
output_card = r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\b.jpg"
edit_for_birthday_card(input_photo, output_card, card_width=1000, card_height=700)