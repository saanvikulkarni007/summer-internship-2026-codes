import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'dataset'

face_samples = []
ids = []

for imagePath in [os.path.join(path,f)
                  for f in os.listdir(path)]:

    PIL_img = Image.open(imagePath).convert('L')

    img_numpy = np.array(PIL_img,'uint8')

    id = int(os.path.split(imagePath)[-1].split(".")[1])

    face_samples.append(img_numpy)
    ids.append(id)

recognizer.train(
    face_samples,
    np.array(ids)
)

recognizer.write('trainer/trainer.yml')

print("Training Complete")