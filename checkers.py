import tkinter as tk
import webbrowser as wb
import os

themecolor = "grey"
color = "#041E42"

def but01():
    wb.open("https://www.google.com/")
    return

def but02():
    wb.open("https://9anime.to/")
    return

def but03():
    wb.open("https://animepahe.com/")
    return

def but04():
    wb.open("https://youtube.com/")
    return

def but05():
    wb.open("https://soap2day.ac/")
    return

def but06():
    wb.open("https://en.sa1lib.org/")
    return

def but07():
    os.startfile(r"C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Spyder (anaconda3).lnk")
    return

def but08():
    wb.open("https://mail.google.com/mail/u/0/#inbox")
    return

def but09():
    wb.open("https://onionplay.se/")
    return

def start():
    global window
    window = tk.Tk()
    window.geometry("403x230")
    window.title("Panel")
    window.config(bg = themecolor)
    label = tk.Label(window, text = "DESK", font = ("poppins", 8, "bold"), fg = "white", bg = themecolor)
    but1 = tk.Button(window, text= "Google", width = 15, height = 2, bg = "lightgray", fg = color, command = but01)
    but2 = tk.Button(window, text= "9anime", width = 15, height = 2, bg = "lightgray", fg = color, command = but02)
    but3 = tk.Button(window, text= "Animepahe", width = 15, height = 2, bg = "lightgray", fg = color, command = but03)
    but4 = tk.Button(window, text= "Youtube", width = 15, height = 2, bg = "lightgray", fg = color, command = but04)
    but5 = tk.Button(window, text= "Soap2day", width = 15, height = 2, bg = "lightgray", fg = color, command = but05)
    but6 = tk.Button(window, text= "Z library", width = 15, height = 2, bg = "lightgray", fg = color, command = but06)
    but7 = tk.Button(window, text= "Python", width = 15, height = 2, bg = "lightgray", fg = color, command = but07)
    but8 = tk.Button(window, text= "Gmail", width = 15, height = 2, bg = "lightgray", fg = color, command = but08)
    but9 = tk.Button(window, text= "Onionplay", width = 15, height = 2, bg = "lightgray", fg = color, command = but09)
    label.grid(row = 0, column = 1, padx = 10, pady = 10)
    but1.grid(row = 1, column = 0, padx = 10, pady = 10)
    but2.grid(row = 1, column = 1, padx = 10, pady = 10)
    but3.grid(row = 1, column = 2, padx = 10, pady = 10)
    but4.grid(row = 2, column = 0, padx = 10, pady = 10)
    but5.grid(row = 2, column = 1, padx = 10, pady = 10)
    but6.grid(row = 2, column = 2, padx = 10, pady = 10)
    but7.grid(row = 3, column = 0, padx = 10, pady = 10)
    but8.grid(row = 3, column = 1, padx = 10, pady = 10)
    but9.grid(row = 3, column = 2, padx = 10, pady = 10)
    
    window.mainloop()


start()