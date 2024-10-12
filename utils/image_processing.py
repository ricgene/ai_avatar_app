import cv2
import dlib
from PIL import Image
import numpy as np

detector = dlib.get_frontal_face_detector()

def extract_face(image_path):
    image = cv2.imread(image_path)
    faces = detector(image)
    if len(faces) > 0:
        face = faces[0]
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        face_image = image[y:y+h, x:x+w]
        return cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
    else:
        return None

def create_composite_image(image_paths):
    faces = []
    for path in image_paths:
        face = extract_face(path)
        if face is not None:
            faces.append(face)

    if faces:
        composite_face = np.hstack(faces)
        composite_image = Image.fromarray(composite_face)
        return composite_image
    else:
        return None
