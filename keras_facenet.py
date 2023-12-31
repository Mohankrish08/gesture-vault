import cv2
import numpy as np 
from mtcnn.mtcnn import MTCNN
import os

class FACELOADING:
    def __init__(self, directory):
        self.directory = directory
        self.target_size = (224, 224)
        self.X = []
        self.Y = []
        self.detector = MTCNN()

    def extract_face(self, filename):
        img = cv2.imread(filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x, y, w, h = self.detector.detect_faces(img)[0]['box']
        face = img[y:y+h, x:x+w]
        face_arr = cv2.resize(face, self.target_size)
        return face_arr

    def load_faces(self, dir):
        FACES = []
        try:
            single_face = self.extract_face(dir)
            FACES.append(single_face)
        
        except Exception as e:
                pass
        return FACES

    def load_classes(self):
        for path in os.listdir(self.directory):
            #path = os.path.join(self.directory, sub_dir)
            FACES = self.load_faces(path)
            labels = [path for _ in range(len(FACES))]
            print(f"Loaded successfully: {len(labels)}")
            self.X.extend(FACES)
            self.Y.extend(labels)



        return np.asarray(self.X), np.asarray(self.Y)
    
def mtcnn(img_dir):
    faceloading = FACELOADING(img_dir)
    X, Y = faceloading.load_classes()
    return X, Y


x,y = mtcnn('E:\\GitHub\\gesture-vault\\images')
print(x)
print(y)   


