import cv2
from datetime import datetime

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

# Load Haar Cascade
faceCascade = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml'
)

# ID to Name mapping
names = {
    1: "Saanvi",
    2: "Rahul",
    3: "Amit"
}

# Start webcam
cam = cv2.VideoCapture(0)

cam.set(3, 640)  # width
cam.set(4, 480)  # height

print("Face Recognition Started...")
print("Press ESC to Exit")

while True:

    ret, img = cam.read()

    if not ret:
        print("Failed to access camera")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:

        # Draw rectangle around face
        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Predict face
        id, confidence = recognizer.predict(
            gray[y:y + h, x:x + w]
        )

        # Convert confidence to accuracy %
        accuracy = round(max(0, min(100, 100 - confidence)))

        if accuracy >= 60:
            name = names.get(id, "Unknown")
        else:
            name = "Unknown"

        # Current date and time
        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Display Name
        cv2.putText(
            img,
            f"Name: {name}",
            (x, y - 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # Display Accuracy
        cv2.putText(
            img,
            f"Accuracy: {accuracy}%",
            (x, y - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        # Display Timestamp
        cv2.putText(
            img,
            timestamp,
            (x, y + h + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1
        )

    cv2.imshow(
        "Real-Time Face Recognition",
        img
    )

    # ESC key to exit
    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()