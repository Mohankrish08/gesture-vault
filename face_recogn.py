import face_recognition
import os
import numpy as np
import pickle
import cv2
from config import cfg


class FaceRec():

    def __init__(self, filepath='.\Project', embedding_path='.\embeddings.pkl'):
        self.faces = []
        self.personName = []

        for i in os.listdir(filepath):
            self.personName.append(os.path.splitext(i)[0])
        print('--------------------------------')
        print(self.personName)
        print('--------------------------------')


    def MatchTheFace(self,img, embedding_path='.\embeddings.pkl'):

        try:   
            with open(embedding_path, 'rb') as file:
                embeddings = pickle.load(file)
        except Exception as e:
            print(e)

        facesInFrame = face_recognition.face_locations(img)
        encodeFacesInFrame = face_recognition.face_encodings(img, facesInFrame)

        for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame) :
            matches = face_recognition.compare_faces(embeddings, encodeFace, tolerance=cfg["tolerance"])
            facedis = face_recognition.face_distance(embeddings, encodeFace)
            #print(facedis)
            matchIndex = np.argmin(facedis)

            if matches[matchIndex] :
                name = self.personName[matchIndex]
                #self.currentUser.append(name)
                print(name)
                faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                faces = faceCascade.detectMultiScale(img,1.3,3)
            

                if len(faces)==1:

                    for(x,y,w,h) in faces:
                        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),5)
                        #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        #cv2.rectangle(frame, (x1, y2-25), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img , name, (x+6, y-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                if name in self.personName:
                    #print(name)
                    return True, name
        return False, ''
                    

        
    



