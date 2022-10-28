"""
Code length = ~750 

Instructions: (Latest)
    1) To open camera on your phone through "IPWebcam app", type the url except http and /video.
       To use the same url again just type 'p' in the entry box.
    2) To click the images, press the capture button, it will open a window where you can crop your texts.
    3) Press spacebar to exit from cropping window.
    4) A new window named as recognized text will automatically open to show you the recognized text.
    5) To save the text click save all and to delete a particular text click the text and then delete.

Version: 1.0.0:
    1) Built basic structure
    2) Added basic GUI

Version: 1.2.0:
    1) Added ip checker and reduced chances of crashing.
    2) Added a functions to select and write text in the main file.
    3) Added environment cleaner to delete temporary files.
    4) Added function to load previous ip without writing it.
    5) The windows close automatically.

Version: 1.3.0
    1) Added splash screens
    2) Improved GUI
    3) csvfile opens automatically when application is closed
    4) Removed extra blank spaces bug in csv file.
    5) Added loading screens

Version: 1.3.1
    1) Added system for re ordering elements.
    
"""
#-----------------------------------------------------------------------------
# IMPORTING MODULES-----------------------------------------------------------
#-----------------------------------------------------------------------------
import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import pytesseract
from tkinter import messagebox as msg
import pickle
import os

#assigning tesseract.exe location
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

#-----------------------------------------------------------------------------
# ASSIGNING GLOBAL VARIABLES--------------------------------------------------
#-----------------------------------------------------------------------------
img_counter = 0
List = []
theme_color = "#25383C"
accent_color = "#25383C"
font1 = "Bahnschrift SemiCondensed"
font2 = "Microsoft YaHei Light"
used = False
saved = False
used_app = False
situation = True

#-----------------------------------------------------------------------------
# GUI FUNCTIONS---------------------------------------------------------------
#-----------------------------------------------------------------------------
def instruction_screen():
    global used, var1
    used = True
    global iwin
    iwin = tk.Tk()
    iwin.geometry("400x200")
    iwin.title("Instructions")
    iwin.config(bg = theme_color)
    laberuuu = tk.Label(iwin, text = "Please use spacebar to exit the cropping window",
                        font = ("Microsoft YaHei Light", 12),
                        bg = theme_color, fg = "white")
    laberuuu.pack(pady = 50)
    laberuuu2 = tk.Button(iwin, text = "Got it!", font = ("Microsoft YaHei Light", 9),
                         bg = "white", fg = theme_color, command = child_func_2,
                         width = 25)
    laberuuu2.pack()
    var1 = tk.IntVar()
    iwin.mainloop()
    return
def child_func_2():
    iwin.destroy()
    crop_the_thing(img_name)
    return
def load_screen():
    global swin
    cv2.destroyAllWindows()
    swin = tk.Tk()
    swin.geometry("400x200")
    swin.title("Automated Data Entry")
    swin.config(bg = theme_color)
    laberuchan = tk.Label(swin, text = "Identifying text...", 
                          font = ("Microsoft YaHei Light",18),
                          bg = theme_color, fg = "white")
    laberuchan.pack(pady = 50)
    swin.after(1000, child_func)
    swin.mainloop()
    return
def child_func():
    save_pickle(List)
    return
def choice1():
    troot.destroy()
    nrecognized_text1()
    return
def choice2():
    troot.destroy()
    nrecognized_text()
    return
def tkinter_choice():
    global troot
    troot = tk.Tk()
    troot.geometry("400x200")
    troot.config(bg = theme_color)
    label = tk.Label(troot, text = "Would you like to re arrange your files?", 
                     bg = theme_color, fg = "white", font = (font1, 12))
    label.pack(pady = 50)
    butyes = tk.Button(troot, text = "yes, i would!", font = (font1, 11), fg = theme_color, bg = "white",
                       width = 20, command = choice1)
    butyes.pack(side = tk.LEFT, padx = 20)
    butno = tk.Button(troot, text = "No", font = (font1, 11), fg = theme_color, bg = "white",
                       width = 20, command = choice2)
    butno.pack(side = tk.RIGHT, padx = 20)
    troot.mainloop()
    return
def save_pickle(lst):
    swin.destroy()
    pickle.dump(lst, open("tempfile.bin", "wb"))
    tkinter_choice()
    return
def nadd_task(event):
    t = ent1.get()
    if t != "":
        list_box.insert(tk.END, t)
        ent1.delete(0, tk.END)
    else:
        msg.showwarning("Warning!", message = "Field cannot be empty.")
    return
def add_task():
    t = ent1.get()
    if t != "":
        list_box.insert(tk.END, t)
        ent1.delete(0, tk.END)
    else:
        msg.showwarning("Warning!", message = "Field cannot be empty.")
    return
def del_task():
    try:
        task_index = list_box.curselection()[0]
        list_box.delete(task_index)
    except:
        msg.showwarning("Warning!", message = "Deleted task should be selected!")
    return
def load_task():
    try:
        tt = pickle.load(open("tempfile.bin", "rb"))
        list_box.delete(0, tk.END)
        for i in tt:
            if i != '':
                list_box.insert(tk.END, i)
            else:
                list_box.insert(tk.END, "## Unrecognized text ##")
    except:
        msg.showwarning("Warning", message = "List is empty")
    return
def save_task():
    global saved
    tt = list_box.get(0, list_box.size())
    write_file(tt)
    # list_box.delete(0, tk.END)
    msg.showinfo("Success!", message = "Your files were saved successfully!")
    os.remove("tempfile.bin")
    proot.destroy()
    saved = True
    return
def on_closing():
    global proot
    global saved
    if saved == False:
        msg.showwarning("Unsaved Changes", message= "You have not saved your work! Please go back and save it")
    return
def paste(event):
    lb1 = list_box
    n1 = lb1.curselection()
    item1 = lb1.get(n1)
    lb2.insert(tk.END, item1)
    lb1.delete(n1)
    return 
def copy(event):
    lb1 = list_box
    n1 = lb2.curselection()
    item1 = lb2.get(n1)
    lb1.insert(tk.END, item1)
    lb2.delete(n1)
    return
def nrecognized_text():
    global ent1
    global list_box
    global proot
    global used_app
    global lb2
    used_app = True
    proot = tk.Tk()
    proot.config(bg = theme_color)
    proot.title("Recognized text")
    #Making a frame in to combine scrollbar and listbox and to scroll it
    furame = tk.Frame(proot, bg = theme_color)
    furame.grid(row = 2, column = 0)   
    s_frame = tk.Frame(proot)
    s_frame.grid(row = 0 , column = 0) 
    a_frame = tk.Frame(proot)
    a_frame.grid(row = 0, column = 1)
    e_frame = tk.Frame(proot, bg = theme_color)
    e_frame.grid(row = 1, column = 0)    
    #Creating widgets
    list_box = tk.Listbox(s_frame, font = ('poppins', 11), height = 15, width = 100,
                          bg = accent_color, selectbackground = '#193f56', fg = "white")
    list_box.pack(padx = 2, pady = 2, side = tk.LEFT)   
    ent1 = tk.Entry(e_frame, width = 115, font = ("poppins", 10, "bold"))
    ent1.grid(row = 1, column = 1, pady = 5)   
    but1 = tk.Button(furame, text = "Add", width =25, height = 5,  command = add_task,
                     fg = "white", bg = "#195356")
    but1.grid(row = 1, column = 0, padx = 2, pady = 2)   
    but4 = tk.Button(furame, text = "Save All", width = 25, fg = "white", height = 5,
                     bg = "#195356", command = save_task)
    but4.grid(row = 1, column = 1, padx = 2, pady = 2)    
    but2 = tk.Button(furame, text = "Delete", width = 25, fg = "white", height = 5,
                     bg = "darkred", command = del_task)
    but2.grid(row = 1, column = 2, padx = 2, pady = 2)
    load_task()    
    #creating scrollbar
    scrl = tk.Scrollbar(s_frame, bg = "#193f56")
    scrl.pack(side = tk.RIGHT, fill = tk.Y)    
    #making scrollbar functional
    list_box.config(yscrollcommand = scrl.set)
    scrl.config(command = list_box.yview)
    #Listening enter key
    proot.bind('<Return>', nadd_task)
    proot.protocol("WM_DELETE_WINDOW", on_closing)
    proot.mainloop()
    return
def load_task1():
    try:
        tt = pickle.load(open("tempfile.bin", "rb"))
        list_box1.delete(0, tk.END)
        for i in tt:
            if i != '':
                list_box1.insert(tk.END, i)
            else:
                list_box1.insert(tk.END, "## Unrecognized text ##")
    except:
        msg.showwarning("Warning", message = "List is empty")
    return
def save_task101():
    global saved
    pproot.destroy()
    tt = list_box1.get(0, list_box1.size())
    if tt == ():
        tkinter_warning2()
    else:
        write_file(tt)
        msg.showinfo("Success!", message = "Your files were saved successfully!")
        os.remove("tempfile.bin")
        proot.destroy()
        saved = True
    return
def tkinter_warning():
    global pproot
    pproot = tk.Tk()
    pproot.geometry("400x200")
    pproot.config(bg = theme_color)
    label = tk.Label(pproot, text = "Are you sure you want to go with the non arranged files?", 
                     bg = theme_color, fg = "white", font = (font1, 12))
    label.pack(pady = 50)
    butyes = tk.Button(pproot, text = "yes, go ahead!", font = (font1, 11), fg = theme_color, bg = "white",
                       width = 25, command = save_task101)
    butyes.pack()
    pproot.mainloop()
    
def tkinter_warning2():
    global pproot
    pproot = tk.Tk()
    pproot.geometry("400x200")
    pproot.config(bg = theme_color)
    label = tk.Label(pproot, text = "Empty files cannot be saved!", 
                     bg = theme_color, fg = "white", font = (font1, 12))
    label.pack(pady = 50)
    pproot.mainloop()
    
def del_task1():
    try:
        task_index = list_box1.curselection()[0]
        list_box1.delete(task_index)
    except:
        msg.showwarning("Warning!", message = "Deleted task should be selected!")
    return
def save_task102():
    global saved
    tt = lb21.get(0, lb21.size())
    if tt == ():
        tkinter_warning2()
    else:
        write_file(tt)
        # list_box.delete(0, tk.END)
        msg.showinfo("Success!", message = "Re arranged files saved successfully!")
        os.remove("tempfile.bin")
        proot.destroy()
        saved = True
    return
def add_task1():
    t = ent11.get()
    if t != "":
        list_box1.insert(tk.END, t)
        ent11.delete(0, tk.END)
    else:
        msg.showwarning("Warning!", message = "Field cannot be empty.")
    return
def nadd_task1(event):
    t = ent11.get()
    if t != "":
        list_box1.insert(tk.END, t)
        ent11.delete(0, tk.END)
    else:
        msg.showwarning("Warning!", message = "Field cannot be empty.")
    return
def paste1(event):
    lb1 = list_box1
    n1 = lb1.curselection()
    item1 = lb1.get(n1)
    lb21.insert(tk.END, item1)
    lb1.delete(n1)
    return 

def copy1(event):
    global list_box1
    global lb21
    lb1 = list_box1
    n1 = lb21.curselection()
    item1 = lb21.get(n1)
    lb1.insert(tk.END, item1)
    lb21.delete(n1)
    return

def nrecognized_text1():
    global used_app
    global proot
    proot = tk.Tk()
    proot.config(bg = theme_color)
    proot.title("Recognized text")
    used_app = True
    
    #proot
    p_frame1 = tk.Frame(proot, bg = theme_color)
    p_frame1.grid(row = 0, column = 0)
    
    p_frame2 = tk.Frame(proot, bg = theme_color)
    p_frame2.grid(row = 1, column = 0, pady = 15)
    
    p_frame3 = tk.Frame(proot, bg = theme_color)
    p_frame3.grid(row = 2, column = 0)
    
    #p_frame1
    p_l_frame = tk.Frame(p_frame1, bg = theme_color)
    p_l_frame.grid(row = 0, column = 0)
    
    #p_l_frame
    p_l_frame1 = tk.Frame(p_l_frame, bg = theme_color)
    p_l_frame1.grid(row = 0)
    
    p_l_frame2 = tk.Frame(p_l_frame, bg = theme_color)
    p_l_frame2.grid(row = 1)
    
    p_l_frame3 = tk.Frame(p_l_frame, bg = theme_color)
    p_l_frame3.grid(row = 2)
    
    #p_frame1
    p_r_frame = tk.Frame(p_frame1, bg = theme_color)
    p_r_frame.grid(row = 0, column = 1)
    
    #p_r_frame
    p_r_frame1 = tk.Frame(p_r_frame, bg = theme_color)
    p_r_frame1.grid(row = 0)
    
    p_r_frame2 = tk.Frame(p_r_frame, bg = theme_color)
    p_r_frame2.grid(row = 1)
    
    p_r_frame3 = tk.Frame(p_r_frame, bg = theme_color)
    p_r_frame3.grid(row = 2)
    
    #Creating widgets
    label_kun1 = tk.Label(p_l_frame1, text = "Recognized Text Column", font = (font1, 11),
                          bg = theme_color, fg = "white")
    label_kun1.pack()
    global list_box1, lb21
    list_box1 = tk.Listbox(p_l_frame2, font = ('poppins', 11), height = 15, width = 60,
                          bg = accent_color, selectbackground = '#193f56', fg = "white")
    list_box1.pack(side = tk.LEFT, padx = 2)
    but41 = tk.Button(p_l_frame3, text = "Save", width = 55, bg = "lightgray", height = 3,
                      fg = theme_color, font = (font1, 11), command = tkinter_warning)
    but41.pack(pady = 5)
    
    label_kun2 = tk.Label(p_r_frame1, text = "Re-arranged Recognized Text Column", font = (font1, 11),
                          bg = theme_color, fg = "white")
    label_kun2.pack()   
    lb21 = tk.Listbox(p_r_frame2, font = ('poppins', 11), height = 15, width = 60,
                     bg = accent_color, selectbackground = '#193f56', fg = "white")
    lb21.pack(side = tk.LEFT, padx = 2)
    but51 = tk.Button(p_r_frame3, text = "Save", width = 55, bg = "lightgray", height = 3,
                      fg = theme_color, font = (font1, 11), command = save_task102)   
    but51.pack(pady = 5)
    
    smol_label = tk.Label(p_frame2, text = "Text:", font = (font1, 11),
                          bg = theme_color, fg = "white")
    smol_label.pack(side = tk.LEFT)
    global ent11
    ent11 = tk.Entry(p_frame2, width = 84, font = (font2, 11, "bold"))
    ent11.pack(side = tk.LEFT, padx = 20)  
    but11 = tk.Button(p_frame2, text = "Add", fg = theme_color, bg = "lightgray", width = 20,
                      command = add_task1)
    but11.pack(side = tk.RIGHT)   
    but21 = tk.Button(p_frame3, text = "Delete", width = 28, fg = "white", height = 2,
                      bg = "darkred", font = (font2, 11), command = del_task1)
    but21.grid(padx = 2, pady = 5)
    load_task1()
    
    #Making a frame in to combine scrollbar and listbox and to scroll it
    furame = tk.Frame(proot, bg = theme_color)
    furame.grid(row = 2, column = 0)
    
    #creating scrollbar
    scrl = tk.Scrollbar(p_l_frame2, bg = "#193f56")
    scrl.pack(side = tk.RIGHT, fill = tk.Y, padx = 3)  
    
    scrl1 = tk.Scrollbar(p_r_frame2, bg = "#193f56")
    scrl1.pack(side = tk.RIGHT, fill = tk.Y, padx = 3) 
    
    #making scrollbar functional
    list_box1.config(yscrollcommand = scrl.set)
    scrl.config(command = list_box1.yview)
    
    lb21.config(yscrollcommand = scrl1.set)
    scrl1.config(command = lb21.yview)
    
    #reordering stuffs
    list_box1.bind("<Double-Button>", paste1)
    lb21.bind("<Double-Button>", copy1)
    
    proot.bind('<Return>', nadd_task1)
    proot.protocol("WM_DELETE_WINDOW", on_closing)
    
    proot.mainloop()


#-----------------------------------------------------------------------------
def another_func():
    but01.config(state = tk.DISABLED)
    but02.config(state = tk.DISABLED)
    os.startfile("csvfile.csv")
    twin.destroy()
    window.destroy()
    return
def an_func():
    labelchan.config(text = "Goodbye!")
    but01.config(state = tk.DISABLED)
    but02.config(state = tk.DISABLED)
    twin.after(1000, children)
    return
def children():
    twin.destroy()
    window.destroy()
    return
def open_file():
    if used_app == True:
        global twin
        global labelchan
        global but01
        global but02
        twin = tk.Tk()
        twin.geometry("400x200")
        twin.config(bg = theme_color)
        labelchan = tk.Label(twin, text = "Would you like to open the saved text file?",
                             font = ("Bahnschrift SemiCondensed", 15, "bold"),
                             fg = "white", bg = theme_color)
        labelchan.pack(pady = 50)
        framechan = tk.Frame(twin, bg = theme_color)
        framechan.pack()
        but01 = tk.Button(framechan, text = "Yes", font = ("Microsoft YaHei Light", 9),
                          fg = theme_color, bg = "white", command = another_func,
                          width = 17)
        but01.grid(row = 0, column = 0, padx = 10)
        but02 = tk.Button(framechan, text = "No", font = ("Microsoft YaHei Light", 9),
                          fg = theme_color, bg = "white", command = an_func,
                          width = 17)
        but02.grid(row = 0, column = 1, padx = 10)
        twin.mainloop()
    else:
        window.destroy()

#-----------------------------------------------------------------------------
# TEXT RECOGNIZER FUNCTIONS---------------------------------------------------
#-----------------------------------------------------------------------------
def mouse_crop(event, x, y, flags, param):
    try:
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
                gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                identify_text(gray, roi)
        if cropping:
            cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (79,75,58), 2)
            cv2.imshow("image", i)
    except:
        pass

def identify_text(gray, frame):
    global ptext
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
        ptext = pytesseract.image_to_string(cropped)
        #cleaning the text
        bad_chars = ['\n', '\x0c']
        for i in bad_chars :
            ptext = ptext.replace(i, '')
        word = str(ptext).strip()
        List.append(word)
    return

#-----------------------------------------------------------------------------
# CAMERA RELATED FUNCTIONS----------------------------------------------------
#-----------------------------------------------------------------------------
def show_frame():
    try:
        global resize
        ret, frame = cap.read()
        resize = cv2.resize(frame, (640, 480), interpolation = cv2.INTER_LINEAR)
        cv2image = cv2.cvtColor(resize, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(3, show_frame)
        but2.config(state = tk.DISABLED)
        t_entry.config(state = tk.DISABLED)
        but.config(state = tk.NORMAL)
        laberu.config(text = "")
        laberu2.config(text = "")
    except:
        msg.showerror("Disconnnected!", message = "Error while connecting to camera!")
    return
def take_screenshot():
    global img_name
    global img_counter
    img_name = "opencv_frame_{}.jpeg".format(img_counter)
    cv2.imwrite(img_name, resize)
    img_counter += 1
    if used == False:
        instruction_screen()
    else:
        crop_the_thing(img_name)
def crop_the_thing(aa):
    global used
    used = True
    global x_start, y_start, x_end, y_end, cropping
    cropping = False
    x_start, y_start, x_end, y_end = 0, 0, 0, 0
    global image
    image = cv2.imread(aa)
    global oriImage
    oriImage = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_crop)
    show_camera()
    return
def show_camera():
    while cv2.waitKey(1) != ord(' '):
    #while cv2.getWindowProperty('image', 0) >= 0:
        global i
        i = image.copy()
        if not cropping:
            cv2.imshow("image", image)
        cv2.waitKey(1)
    load_screen()
    return

#-----------------------------------------------------------------------------
# FILE WRITER FUNCTION--------------------------------------------------------
#-----------------------------------------------------------------------------
def write_file(q):
    try:
        global fff
        with open("csvfile.csv", 'a') as fff:
            for j in q:
                fff.write(j)
                fff.write("\n")
        cleaner()
    except:
        msg.showerror("Error", message = "An unkown error occured while writing files")

#-----------------------------------------------------------------------------
# MAIN SCREEN FUNCTIONS-------------------------------------------------------
#-----------------------------------------------------------------------------
def mn_window():
    global window
    croot.destroy()
    #Set up GUI
    window = tk.Tk()  #Makes main window
    window.wm_title("Connection Screen")
    window.config(background=theme_color)
    window.geometry("635x615")
    window.resizable(0,0)
    #Frame for camera
    imageFrame = tk.Frame(window, width=600, height=500)
    imageFrame.grid(row=0, column=0, padx=10, pady=7)
    #Capture video frames
    global lmain
    lmain = tk.Label(imageFrame, bg = theme_color)
    lmain.grid(row=0, column=0)
    #Frame for buttons, text extra
    sliderFrame = tk.Frame(window, width=600, height=130, background= theme_color)  
    sliderFrame.grid(row = 600, column=0, padx=10, pady=5)
    global t_entry
    t_entry = tk.Entry(sliderFrame, width = 43,
                       font = ("poppins", 10, "bold"))
    t_entry.place(x = 118, y = 2)
    global but2
    but2 = tk.Button(sliderFrame, text = "OK", width = 5, font = ("poppins", 10, "bold"),
                     command = get_urln)
    but2.place(x = 437, y = -3)
    #Buttons
    global but
    but = tk.Button(sliderFrame, 
                    text = "Capture", 
                    font = ("poppins",10,"bold"), 
                    width = 45, 
                    height = 2, 
                    command = take_screenshot,
                    state = tk.DISABLED)
    but.place(x = 118, y = 30)
    global laberu
    global laberu2
    laberu = tk.Label(sliderFrame, text = "Type the numbers of ip address for eg: 192.253.2.981:8080",
                      font = ('poppins', 12),
                      fg = "white",
                      bg = theme_color)
    laberu.place(x = 93, y = 80)
    laberu2 = tk.Label(sliderFrame, text = "or type 'p' to use the same ip address again",
                       font = ('poppins', 12),
                       fg = "white",
                       bg = theme_color)
    laberu2.place(x = 151, y = 105)
    window.bind("<Return>", get_url)
    window.protocol("WM_DELETE_WINDOW", open_file)
    return

#-----------------------------------------------------------------------------
# USER FRIENDLY FUNCTIONS-----------------------------------------------------
#-----------------------------------------------------------------------------
def prev_ip(ip):
    iplst = [ip]
    with open("ip.bin", "wb") as f:
        pickle.dump(iplst, f)
    return
def load_ip():
    with open("ip.bin", "rb") as f:
        lst = pickle.load(f)
    return lst[0]
def check_url(url):
    xyz = url.split(".")
    wxy = xyz[3].split(":")
    tot = xyz + wxy
    tot.pop(3)
    for i in tot:
        try:
            int(i)
        except:
            msg.showerror("Incorrect IP", message = "You have entered wrong ip address!")
    if len(tot) == 5:
        return url
    else:
        msg.showerror("Incorrect URL", message = "You have entered wrong IP address!")
def get_url(event):
    try:
        global cap
        global img_name
        u = t_entry.get()
        t_entry.delete(0, tk.END)
        u1 = str(u)
        if u1 == "p":
            try:
                url = load_ip()
                cap = cv2.VideoCapture(url)
                show_frame()
            except:
                msg.showerror("Error", message = "No previous IP address found!")
        elif u1 == "s":
            pic = "pic1.jpeg"
            img_name = pic
            if used == False:
                instruction_screen()
            else:
                crop_the_thing(pic)
        else:
            alpha = check_url(u1)
            if alpha == u1:
                url = 'http://' + u1 + '/video'
                prev_ip(url)
                cap = cv2.VideoCapture(url)
                show_frame()
    except:
        msg.showerror("Error!", message = "Make sure you have entered correct ip of your ipcamera!")
    return
def get_urln():
    try:
        global cap
        global img_name
        u = t_entry.get()
        t_entry.delete(0, tk.END)
        u1 = str(u)
        if u1 == "p":
            try:
                url = load_ip()
                cap = cv2.VideoCapture(url)
                show_frame()
            except:
                msg.showerror("Error", message = "No previous IP address found!")
        elif u1 == "s":
            pic = "pic1.jpeg"
            img_name = pic
            if used == False:
                instruction_screen()
            else:
                crop_the_thing(pic)
        else:
            alpha = check_url(u1)
            if alpha == u1:
                url = 'http://' + u1 + '/video'
                prev_ip(url)
                cap = cv2.VideoCapture(url)
                show_frame()
    except:
        msg.showerror("Error!", message = "Make sure you have entered correct ip of your ipcamera!")
    return
def cleaner():
    try:
        fff.close()
        List.clear()
        list_box.delete(0, tk.END)
        for i in range(0, img_counter + 1):
            os.remove(f"opencv_frame_{i}.jpeg")
    except:
        pass

# PROGRAM INITIATOR-----------------------------------------------------------
croot = tk.Tk()
croot.title("Opening application")
croot.geometry("400x200")
croot.config(bg = theme_color)
label1 = tk.Label(croot, text = "Automated Data Entry", bg = theme_color, fg = "white", 
                  font = ("Bahnschrift SemiCondensed", 18, "bold"))
#label1.pack(pady = 50)
label1.place(x = 93, y = 60)
label2 = tk.Label(croot, text = "Welcome", bg = theme_color, fg = "white",
                  font = ("Microsoft YaHei Light", 12))
label2.place(x = 155, y = 100)

croot.after(2500, mn_window)

tk.mainloop()

# PROGRAM ENDER---------------------------------------------------------------
try:
    cap.release()
    cleaner()
except:
    pass

"""
------------------------------------
Version: 1.0.0
Completed the project on: 02/12/2021
--------------UPDATE----------------
Version: 1.2.0
Complete the project on: 17/12/2021
--------------UPDATE----------------
Version: 1.3.0
Complete the project on: 01/01/2022
--------------UPDATE----------------
Version: 1.3.1
Complete the project on: 05/01/2022
------------------------------------

Name of Project: Automated Data Entry
By: Abdulla Shahzan
"""