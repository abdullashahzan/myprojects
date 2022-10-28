def detect_facial_features(x,y):
    import cv2
    downloaded_data = cv2.CascadeClassifier(x)
    downloaded_data2 = cv2.CascadeClassifier(y)
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        coordinates = downloaded_data.detectMultiScale(gray)
        for (x,y,w,h) in coordinates:
            cv2.rectangle(frame, (x,y), (x+w , y+h), (0,255,0), 2)
            sub_frame = frame[y:y+h , x:x+w]
            gray2 = cv2.cvtColor(sub_frame, cv2.COLOR_BGR2GRAY)
            coordinates2 = downloaded_data2.detectMultiScale(gray2, scaleFactor = 1.7 , minNeighbors = 19)
            for (a,b,c,d) in coordinates2:
                cv2.rectangle(sub_frame, (a,b), (a+c , b+d), 2)
            if len(coordinates2)>0:
                cv2.putText(frame, "text", (x , y + h + 40), fontScale = 3, fontFace = cv2.FONT_HERSHEY_PLAIN, color = (255,255,255))
        cv2.imshow('videoWindow', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    