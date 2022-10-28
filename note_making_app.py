import tkinter as tk
from tkinter.scrolledtext import ScrolledText as s
import tkinter.messagebox as m
import pickle

root = tk.Tk()
root.title("Note maker")
root.configure(bg = "lightblue")
root.geometry("700x500")

def save():
    listo = []
    a = text.get('1.0', tk.END)
    aa = ent1.get()
    b = a.split(" ")
    if b == ['\n'] or aa == "":
        m.showwarning("Warning", message = "Text or title cannot be empty")
    else:
        listo = [aa, a]
        filenm = aa + '.bin'
        pickle.dump(listo, open(filenm, 'wb'))
        m.showinfo("Saved successfully", message = "Your file was saved successfully")
    ent1.delete(0, tk.END)
    text.delete('1.0', tk.END)
    return 

def load():
    try:
        t = ent1.get()
        filenm = t + '.bin'
        tt = pickle.load(open(filenm, "rb"))
        text.delete('1.0', tk.END)
        for i in tt[1]:
            text.insert(tk.INSERT, i)
    except:
        m.showwarning("Warning", message = "file not found")
    return

furame = tk.Frame(root, bg = "lightblue")
furame.pack()

text = tk.scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 65, height = 18, 
                                    font = ("times new roman", 15))
text.pack()

furame1 = tk.Frame(root, bg = "lightblue")
furame1.pack()

but1 = tk.Button(furame1, text = "save", width = 25, command = save)
but1.grid(row = 0 , column = 0, pady = 10, padx = 10)

but2 = tk.Button(furame1, text = "Load", width = 25, command = load)
but2.grid(row = 0 , column = 1, pady = 10, padx = 10)

ent1 = tk.Entry(furame, width = 50, font = ("poppins", 10, "bold"))
ent1.grid(row = 0, column = 1, padx = 10, pady = 10)

lab = tk.Label(furame, text = "Title:", bg = "lightblue")
lab.grid(row = 0, column = 0, pady = 10)

root.mainloop()

