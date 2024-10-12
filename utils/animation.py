import cv2
import time
import numpy as np

def animate_avatar(images):
    cv2.namedWindow('Avatar Animation', cv2.WINDOW_NORMAL)
    for i in range(50):
        for image in images:
            cv2.imshow('Avatar Animation', image)
            time.sleep(0.1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cv2.destroyAllWindows()

def prepare_images_for_animation(face_images):
    return [cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR) for img in face_images]
