import tkinter as tk
import json, difflib
import webbrowser as wb
 
cmd = json.loads(open("cmds.json").read())
theme = "lightblue"
theme2 = "grey"
found = False
add = False
temlst = []

def start():
    global entry1, text2
    root = tk.Tk()
    root.geometry("400x120")
    root.title("Web shortcut")
    root.config(bg = theme)
    entry1 = tk.Entry(root, width = 40, font = ("poppins", 12), fg = "darkgrey")
    entry1.place(x = 18, y = 50)
    text = tk.Label(root, text = "Type here:", font = ("poppins", 8), bg = theme,fg = theme2)
    text.place(x = 18, y = 30)
    text2 = tk.Label(root, font = ("poppins", 10), bg = theme, fg = theme2)
    text2.place(x = 140, y = 80)
    root.bind("<Return>", fun)
    root.mainloop()
    return

def fun(event):
    global found
    t = entry1.get()
    if add == False:
        word = clean(t)
        keyword(word)
    elif add == True:
        temlst.append(t)
        text2.config(text = "")
        modify(temlst[0], temlst[1])
    entry1.delete(0, tk.END)
    return

def clean(word):
    word = ''.join(e for e in word if e.isalnum() or e == " ").lower().strip().split()
    return word

def keyword(word):
    global add, found
    for i in cmd['data']:
        sim = difflib.SequenceMatcher(None, i['keyword'], word).ratio()
        if sim > 0.4:
            url = i['action']
            wb.open(url)
            found = True
    if found == False:
        wb.open("https://www.google.com/")
        temlst.append(word)
        add = True
        text2.config(text = "Paste new URL")
    else:
        found = False
    return

def modify(name, url):
    global add, found
    d = {}
    d['keyword'] = name
    d['action'] = url
    lst = cmd['data']
    lst.append(d)
    with open("cmds.json", "w") as f:
        json.dump(cmd, f)
    temlst.clear()
    add = False
    return

start()

