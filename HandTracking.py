import cv2
import mediapipe as mp
import time

mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

ptime = 0
ctime = 0

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(frame, handlms, mphands.HAND_CONNECTIONS)
            for iD, lm in enumerate(handlms.landmark):
                height , width, channel = frame.shape
                pixelx , pixely = int(lm.x * width), int(lm.y * height)
                print(iD , pixelx , pixely)
                if iD == 4:
                    cv2.circle(frame, (pixelx, pixely), 15, (255,0,255), cv2.FILLED)
    
    ctime = time.time()
    fps = 1/(ctime - ptime)
    ptime = ctime
    
    cv2.putText(frame, str(int(fps)), (10,30), 3, cv2.FONT_HERSHEY_PLAIN ,(0,255,0), 3)
            
    cv2.imshow('videoWindow', frame)      
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

print("Code ran successfully")