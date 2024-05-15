# importing libraries
import streamlit as st
import cv2
import streamlit_lottie as st_lottie
from streamlit_option_menu import option_menu
import numpy as np
import face_recognition
import requests
import os
import matplotlib.pyplot as plt
from PIL import Image
from config import cfg
import mediapipe as mp
from draw_page import DrawPage
from detect_click import DetectClick
import datetime
from face_recogn import FaceRec
from sqlite import db_connector


# set page confit
st.set_page_config(page_title='Gestura Valut', page_icon=":atm:", layout='wide')

# loading animations
def loader_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# loading assets

home = loader_url('https://lottie.host/6e10a710-c88a-47a0-80bb-66dad468098f/lNisqiGNUh.json')

# function
def main():
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cfg["screen_x"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cfg["screen_y"])

    dwPg = DrawPage(cfg["pages"])

    coords = dwPg.getCoordintates()

    detClick = DetectClick([s[-1] for s in coords])

    faceRec = FaceRec()
    #face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    mp_hands = mp.solutions.hands.Hands(
        min_detection_confidence = cfg["min_detection_confidence"],
        min_tracking_confidence = cfg["min_tracking_confidence"],
        max_num_hands = cfg["max_num_hands"]
    )

    with mp_hands as hands:

        while cap.isOpened():
            success, image = cap.read()
            if not success:
              print("Ignoring empty camera frame.")
              break


            overlay = cv2.flip(image, 1).copy()
            output = cv2.flip(image, 1).copy()

            if (("face_matched" in cfg and not cfg["face_matched"]) or "face_matched" not in cfg) and cfg["currentpage"] == "Match":
                faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.05, 5)
                cfg["face_matched"], name = faceRec.MatchTheFace(image)
                if cfg['face_matched']:
                    print(name)
                if len(faces)==1:
                    for(x,y,w,h) in faces:
                        cv2.rectangle(output, (x,y), (x+w, y+h), (0,255,0),5)
                        if cfg['face_matched']:
                            cv2.putText(output, name, (x+6, y-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        else:
                            cv2.putText(output, "Unknown", (x+6, y-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cfg["currentpage"] = "Transactions" if cfg["face_matched"] else "FaceRec"
                newott = db_connector('.\Test.csv', name)
                #print(newott)
                st.write(newott)

                

            dwPg.drawThePage(cfg["currentpage"], overlay)

    
            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
            output.flags.writeable = False

            results = hands.process(output)

            output.flags.writeable = True
            output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)

            if results and results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]

                imgH, imgW, imgC = output.shape

              
                xpos, ypos = int(hand.landmark[8].x * imgW), int(hand.landmark[8].y * imgH)

                cv2.circle(overlay, (xpos, ypos), 20, (255, 0, 255), cv2.FILLED)

                
                clickedBtnIndex = detClick.detectClick((xpos, ypos))

                if clickedBtnIndex != None and clickedBtnIndex>-1 and clickedBtnIndex <8:
                    
                    if "endtime" not in cfg:
                        cfg["endtime"] = datetime.datetime.now() + datetime.timedelta(seconds=cfg["btnClickDelay"])
                        cfg["endtime"] = cfg["endtime"].strftime("%H:%M:%S.%f")[:-3]

                    
                    elif cfg["endtime"] <= datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]:
                        cPage = cfg["currentpage"]
                        cfg["currentpage"] = cfg["pages"][cPage]["navigation"][clickedBtnIndex]
                        del cfg["endtime"]

                elif clickedBtnIndex == None and "endtime" in cfg:
                    if "face_matched" in cfg:
                        del cfg["face_matched"]
                    del cfg["endtime"]

            
            alpha = cfg["alpha"]
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

            
            cv2.imshow("Gesture Based - Touchless ATM", output)

            if cv2.waitKey(5) & 0xFF == ord('q') or cfg["currentpage"] == "Exit":
              break

    cap.release()


# Home page 
with st.sidebar:
    with st.container():
        i,j = st.columns((4,4))
        with i:
            st.empty()
        with j:
            st.empty()

    choose = option_menu(
        "Gestura valut",
        ["Home", "ATM"],
        menu_icon='ATM',
        default_index=0,
        orientation='vertical'
    )

if choose == 'Home':

    st.markdown("<h1 style='text-align: center;'> Gestura Vault </h1>", unsafe_allow_html=True)

    st.write('--------')

    st.markdown("""

    Gesture Vault revolutionizes ATM usage by introducing the Touchless ATM Revolution. 
    It offers a seamless, hygienic, and secure transaction experience by allowing users to 
    perform transactions using simple hand movements. This innovative approach to modern banking 
    eliminates the need for physical contact with ATM surfaces, enhancing convenience and safety for customers.

    """, unsafe_allow_html=True)

    st.lottie(home, height=300, key='front')


elif choose == 'ATM':
    if __name__ == "__main__":
        main()