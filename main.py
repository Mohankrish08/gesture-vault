import cv2
from config import cfg
import mediapipe as mp
from draw_page import DrawPage
from detect_click import DetectClick
import datetime
from face_recogn import FaceRec


def main():
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cfg["screen_x"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cfg["screen_y"])

    dwPg = DrawPage(cfg["pages"])

    coords = dwPg.getCoordintates()

    detClick = DetectClick([s[-1] for s in coords])

    faceRec = FaceRec()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

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
                gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.05, 5)
                cfg["face_matched"] = faceRec.MatchTheFace(image) if len(faces) >= 1 else False
                cfg["currentpage"] = "Transactions" if cfg["face_matched"] == True else "FaceRec"

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


if __name__ == "__main__":
    main()