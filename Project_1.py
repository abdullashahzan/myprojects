"""
Raw code for data entry automation
"""

#importing files
import cv2
import pytesseract
import numpy as np 

#assigning tesseract.exe location
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#defining functions
def files(text):
    # Open the file in append mode
    file = open("recognized.txt", "a")
    # Appending the text into file
    file.write(text)
    file.write("\n")
    # Close the file
    file.close  
    return

def identify_text(gray, frame):
    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 100)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Drawing a rectangle on copied image
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Cropping the text block for giving input to OCR
        cropped = frame[y:y + h, x:x + w]
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
        files(text)      
    return

def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished
        refPoint = [(x_start, y_start), (x_end, y_end)]
        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            identify_text(gray, roi)
    if cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (0, 0, 255), 2)
        cv2.imshow("image", i)

def crop_the_thing(aa):
    global x_start, y_start, x_end, y_end, cropping
    cropping = False
    x_start, y_start, x_end, y_end = 0, 0, 0, 0
    image = cv2.imread(aa)
    global oriImage
    oriImage = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_crop)
    while cv2.waitKey(1) != ord('q'): #% 256 != 27:
        global i
        i = image.copy()
        if not cropping:
            cv2.imshow("image", image)
        cv2.waitKey(1)
    # close all open windows
    cv2.destroyAllWindows()
    return

def camera1():
    url = 'http://192.168.8.107:8080/video'
    cap = cv2.VideoCapture(url)
    img_counter = 0
    while(True):
        ret, frame = cap.read()
        if ret is False:
            print("No camera detected")
            break
        resize = cv2.resize(frame, (640, 480), interpolation = cv2.INTER_LINEAR) 
        cv2.imshow('frame',resize)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break
        elif q == ord("s"):
            global img_name
            img_name = "opencv_frame_{}.jpeg".format(img_counter)
            cv2.imwrite(img_name, resize)
            print("{} written!".format(img_name))
            img_counter += 1
            crop_the_thing(img_name)
    cap.release()
    cv2.destroyAllWindows()
    return

camera1()
print("Code Ran Successfully")