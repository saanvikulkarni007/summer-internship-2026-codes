import cv2

face_detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

cam = cv2.VideoCapture(0)

person_id = input("Enter ID: ")

count = 0

while True:
    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        1.3,
        5
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (255,0,0),
            2
        )

        count += 1

        cv2.imwrite(
            f"dataset/User.{person_id}.{count}.jpg",
            gray[y:y+h, x:x+w]
        )

        cv2.imshow("image", img)

    if cv2.waitKey(100) & 0xff == 27:
        break

    elif count >= 50:
        break

cam.release()
cv2.destroyAllWindows()