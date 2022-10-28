#ALL SOURCE CODES CV2
# x and y are any .xml file downloaded from internet 
# a is image url

def detect_video(x):
    import cv2
    downloaded_data = cv2.CascadeClassifier(x)
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        coordinates = downloaded_data.detectMultiScale(gray)
        for (x,y,w,h) in coordinates:
            cv2.rectangle(frame, (x,y), (x+w , y+h), (0,255,0), 2)
        cv2.imshow('videoWindow', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def detect_image(x,a):
    import cv2
    downloaded_data = cv2.CascadeClassifier(x)
    image = cv2.imread(a)
    greyimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    coordinates = downloaded_data.detectMultiScale(greyimg)
    for (x,y,w,h) in coordinates:
        cv2.rectangle(image, (x,y), (x+w , y+h), (0,255,0), 2)
    cv2.imshow("imageWindow", image)
    cv2.waitKey()


def detect_video_2(x,y):
    import cv2
    downloaded_data = cv2.CascadeClassifier(x)
    downloaded_data2 = cv2.CascadeClassifier(y)
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        coordinates = downloaded_data.detectMultiScale(gray)
        coordinates2 = downloaded_data2.detectMultiScale(gray)
        for (x,y,w,h) in coordinates:
            cv2.rectangle(frame, (x,y), (x+w , y+h), (0,255,0), 2)
        for (a,b,c,d) in coordinates2:
            cv2.rectangle(frame, (a,b), (a+c , b+d), (0,0,255), 2)
        cv2.imshow('videoWindow', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def detect_image_2(y,z,a):
    import cv2
    downloaded_data1 = cv2.CascadeClassifier(y)
    downloaded_data2 = cv2.CascadeClassifier(z)
    image = cv2.imread(a)
    greyimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    coordinates1 = downloaded_data1.detectMultiScale(greyimg)
    coordinates2 = downloaded_data2.detectMultiScale(greyimg)
    for (x,y,w,h) in coordinates1:
        cv2.rectangle(image, (x,y), (x+w , y+h), (0,255,0), 2)
    for (a,b,c,d) in coordinates2:
        cv2.rectangle(image, (a,b), (a+c , b+d), (0,0,255), 2)
    cv2.imshow("imageWindow", image)
    cv2.waitKey()


def detect_facialfeature(x,y):     #This one is for smiling only at the moment
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
                cv2.putText(frame, "smiling", (x , y + h + 40), fontScale = 3, fontFace = cv2.FONT_HERSHEY_PLAIN, color = (255,255,255))
        cv2.imshow('videoWindow', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()