import cv2
import numpy as np
import os

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Desired size for all images (width, height)
image_size = (200, 200)

# Load the training images (known faces)
def load_images_from_folder(folder):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            # Resize the image to the desired size
            img_resized = cv2.resize(img, image_size)
            images.append(img_resized)
            labels.append(int(filename.split('_')[0]))  # Extract label from filename
    return images, labels

# Path to the known faces folder
known_faces_folder = 'known_faces'

# Load known faces and their labels
known_images, labels = load_images_from_folder(known_faces_folder)

if len(known_images) == 0:
    raise ValueError("No images found in the 'known_faces' folder. Please ensure it contains images.")

# Train the recognizer (Eigenfaces method)
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.train(known_images, np.array(labels))

# Load an image to recognize
unknown_image = cv2.imread('unknown_person.jpg')

# Check if the image was loaded successfully
if unknown_image is None:
    raise ValueError("The image 'unknown_person.jpg' could not be loaded. Please check the file path and try again.")

# Convert to grayscale
gray = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2GRAY)

# Detect faces in the unknown image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    # Extract the face ROI
    face_roi = gray[y:y+h, x:x+w]
    
    # Resize the face ROI to the size expected by the recognizer (e.g., 200x200)
    face_roi_resized = cv2.resize(face_roi, image_size)
    
    # Recognize the face
    label, confidence = recognizer.predict(face_roi_resized)
    print(confidence,label)
    
    # Set a threshold for recognition confidence
    if confidence < 4000:  # Lower values mean a better match
        label_text = f"Match (ID: {label})"
    else:
        label_text = "No Match"
    
    # Draw a rectangle around the detected face and label it
    cv2.rectangle(unknown_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(unknown_image, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

# Display the result
cv2.imshow('Face Recognition', unknown_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
