import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk

#Functions
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 
    return

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Project Alpha")
window.config(background="#0C5763")
window.geometry("664x615")
window.resizable(0,0)

#Frame for camera
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=7)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

#Frame for buttons, text extra
sliderFrame = tk.Frame(window, width=600, height=100, background= "#0C5763")
sliderFrame.grid(row = 600, column=0, padx=10, pady=5)

#Buttons
but = tk.Button(sliderFrame, text = "Click me", font = ("poppins",10,"bold"), width = 25)
but.place(x = 30, y = 20)

but2 = tk.Button(sliderFrame, text = "Another one", font = ("poppins",10,"bold"), width = 25)
but2.place(x = 350, y = 20)

show_frame()  #Display 2
window.mainloop()  #Starts GUI
cap.release()