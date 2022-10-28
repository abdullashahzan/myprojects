import tkinter as tk
import tkinter.messagebox as msg
import pickle

root = tk.Tk()
root.title("To-do List")

#creating functions
def nadd_task(event):
    t = ent1.get()
    if t != "":
        list_box.insert(tk.END, t)
        ent1.delete(0, tk.END)
    else:
        msg.showwarning("Warning!", message = "Tasks cannot be empty.")
    return

def add_task():
    t = ent1.get()
    if t != "":
        list_box.insert(tk.END, t)
        ent1.delete(0, tk.END)
    else:
        msg.showwarning("Warning!", message = "Tasks cannot be empty.")
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
        tt = pickle.load(open("to-do-list.bin", "rb"))
        list_box.delete(0, tk.END)
        for i in tt:
            list_box.insert(tk.END, i)
    except:
        msg.showwarning("Warning", message = "List is empty")
    return

def save_task():
    tt = list_box.get(0, list_box.size())
    pickle.dump(tt, open("to-do-list.bin", "wb"))
    return

#Making a frame in to combine scrollbar and listbox and to scroll it
furame = tk.Frame(root)
furame.pack()

#Creating widgets
list_box = tk.Listbox(furame, font = ('poppins', 11), height = 15, width = 42,
                      bg = "lightgray")
list_box.pack(padx = 2, pady = 2, side = tk.LEFT)

ent1 = tk.Entry(root, width = 49, font = ("poppins", 10))
ent1.pack(pady = 5)

but1 = tk.Button(root, text = "Add task", width = 49, command = add_task,
                 fg = "grey", bg = "lightblue")
but1.pack()

but3 = tk.Button(root, text = "Load tasks", width = 49 , fg = "grey",
                 bg = "lightblue", command = load_task)
but3.pack()

but4 = tk.Button(root, text = "Save tasks", width = 49, fg = "grey",
                 bg = "lightblue", command = save_task)
but4.pack()

but2 = tk.Button(root, text = "Delete task", width = 49, fg = "white",
                 bg = "darkred", command = del_task)
but2.pack()

#creating scrollbar
scrl = tk.Scrollbar(furame)
scrl.pack(side = tk.RIGHT, fill = tk.Y)

#making scrollbar functional
list_box.config(yscrollcommand = scrl.set)
scrl.config(command = list_box.yview)

#Listening enter key
root.bind('<Return>', nadd_task)

root.mainloop()


