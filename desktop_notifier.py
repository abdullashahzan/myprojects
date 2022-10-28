import tkinter as tk
from plyer import notification as n
import time
from tkinter import messagebox as mm

t = tk.Tk()
t.title("Notification Manager")
t.geometry("450x200")


#Programs

def get_details():
    t = t_entry.get()
    m = t_entry2.get()
    tyme = t_entry3.get()
    
    if t == "" or m == "" or tyme == "":
        mm.showerror("Alert", "All fields are required")
    else:
        tyme_sec = int(float(tyme))*60
        mm.showinfo("Notfication set", "Set notification?")
        time.sleep(tyme_sec)
        n.notify(title = t,
                 message = m,
                 app_name = "Notifier",
                 timeout = 4)


#Creating Labels
t_label = tk.Label(t, text = "Title to Notify", font = ("poppins",10))
t_label.place(x = 12, y = 12)

#Entry 1
t_entry = tk.Entry(t, width = "35", font = ("poppins",10))
t_entry.place(x = 163, y = 14)

#Label 2
t_labe2 = tk.Label(t, text = "Display message", font = ("poppins",10))
t_labe2.place(x = 12, y = 65)

#Entry 2
t_entry2 = tk.Entry(t, width = "35", font = ("poppins",10))
t_entry2.place(x = 163, y = 67)

#Label 3
t_labe3 = tk.Label(t, text = "Set time", font = ("poppins",10))
t_labe3.place(x = 12, y = 125)

#Entry 3
t_entry3 = tk.Entry(t, width = "5", font = ("poppins",10))
t_entry3.place(x = 163, y = 125)

#Label 4
t_labe4 = tk.Label(t, text = "min", font = ("poppins",10))
t_labe4.place(x = 210, y = 125)

#button
but = tk.Button(t , text = "SET TIMER", font = ("poppins",10, "bold"), fg = "#ffffff", bg = "#528DFF", width = 20, relief = "raised", command = get_details)
but.place(x = 110, y = 165)

t.resizable(0,0)
t.mainloop()