import tkinter as tk
import random as r
import webbrowser as wb
import json
from nltk.stem import WordNetLemmatizer as wnl
import os
import difflib
from googlesearch import search as s
import pyjokes

theme_color = "#25383C"
font1 = "Microsoft YaHei Light"
login = False
file = "intents.json"
a = json.loads(open(file).read())
l = wnl()
lstr = []
short_memory = []
word_found = False
formula = 0
correcting = False
searching = False
counter = 0
rcounter = 0
ans_found = False
saved = False

def start():
    global ent, label, root, frame1, frame2, label2, frame3, but, label3
    root = tk.Tk()
    root.geometry("700x350")
    root.title("REM")
    root.config(bg = theme_color)
    frame1 = tk.Frame(root, bg = theme_color)
    frame1.pack()
    frame2 = tk.Frame(root, bg = theme_color)
    frame2.pack()
    frame3 = tk.Frame(root, bg = theme_color)
    frame3.pack()
    label3 = tk.Label(frame1, text = "Conversation tags", font = (font1, 9), bg = theme_color,
                      fg = 'white')
    label3.pack(side = tk.TOP, pady = 10)
    label = tk.Label(frame1, text = "Rem at your service!!", 
                     font = (font1, 15), bg = theme_color, fg = 'white',
                     width = 64, height = 5)
    label.pack(pady = 5)
    label2 = tk.Label(frame2, text = "Type here: ", font = (font1, 11), bg = theme_color, fg = 'white')
    label2.pack()
    ent = tk.Entry(frame2, font = (font1, 10), width = 70)
    ent.pack()
    but = tk.Button(frame3, text = "Talking to Rem...", font = (font1, 14), fg = theme_color,
                    bg = "white", width = 25, command = master_input, state = tk.DISABLED)
    but.pack(pady = 20)
    root.bind("<Return>", simple_letters)
    root.mainloop()
    return

def master_input():
    global login
    if login == True:
        revert()
    else:
        get5responses()
    return

def simple_letters(event):
    ui = ent.get()
    d = ui.strip()
    lui = d.lower()
    a = lui.replace(" ","#")
    b = ''.join(e for e in a if e.isalnum() or e == "#" or e == "+" or e == "-" or e == "/" or e == "*" or e == ".")
    c = b.replace("#", " ")
    if correcting == False:
        ent.delete(0, tk.END)
    if login == False:
        if correcting == True:
            master_input()
        else:
            vocabulary(c)
    elif login == True:
        cmds(c)
    return

def vocabulary(word):
    global theme_color, login
    if word == "1439":
        theme_color = "#800020"
        label.config(text = "Welcome Shahzan!")
        but.config(text = 'Log out', state = tk.ACTIVE)
        login = True
        chng_color("#800020")
    elif word == "close yourself":
        root.destroy()
    elif word == "please tell me a joke":
        while True:
            joke = pyjokes.get_joke(language = "en", category= "neutral")
            if len(joke) < 80:
                label.config(text = joke)
                break
            else:
                continue
    elif difflib.SequenceMatcher(None, word, "how old are you").ratio() > 0.95:
        label.config(text = "65")
    elif word.split(" ")[0] == "color":
        chng_color(word.split(" ")[1])
    else:
        short_mem(word)
    return

def cmds(words):
    word = words.replace(" ", "#")
    word = word.split("#")
    if word[0] == 'command' or word[0] == 'cmd':
        command(word)
    elif word[0] == 'revert':
        revert()
    elif word[0] == '-':
        label.config(text = "Online...")
        subsearch(word[1:])
    else:
        label.config(text = "Can't identify!")
    return

def revert():
    global login, logged_in
    login = False
    logged_in = False
    label.config(text = "Logged out successfully!")
    label2.config(text = "Type here:")
    but.config(text = "Talking to Rem...", state = tk.DISABLED)
    chng_color("#25383C")
    return

def command(listcc):
    try:
        if listcc[1] == "type" and listcc[2] != "" and len(listcc)>2:
            label.config(text = listcc[2:])
        elif listcc[1] == "show" :
            if listcc[2] == 'anime':
                label.config(text = "showing anime...")
                anime_s_window()
            elif listcc[2] == "gmaps":
                label.config(text = "showing google maps...")
                wb.open('https://www.google.com/maps/')
            elif listcc[2] == "ip":
                label.config(text = "showing details...")
                ipa = "".join(listcc[3:])
                ipInfo(ipa)
            elif listcc[2] == "ph":
                label.config(text = "showing details...")
                phn(listcc[3])
            elif listcc[2] == "wifi":
                label.config(text = "showing details...")
                wf()
            elif listcc[2] == "cmd":
                os.startfile('commandsRem.txt')
        elif listcc[1] == "search" or listcc[1] == "-s":
            search = listcc[2:]
            label.config(text = "Searching across internet...")
            sgoogle(search)
        elif listcc[1] == "develop":
            label.config(text = "Stopping GUI...")
            root.after(2000, develop)
        else:
            label.config(text = "Error")
    except:
        label.config(text = "Error1")
    return

def chng_color(color):
    global theme_color
    try:
        theme_color = color
        root.config(bg = theme_color)
        label.config(bg = theme_color)
        frame1.config(bg = theme_color)
        frame2.config(bg = theme_color)
        label.config(bg = theme_color)
        label2.config(bg = theme_color)
        frame3.config(bg = theme_color)
        but.config(fg = theme_color)
        label3.config(bg = theme_color)
    except:
        try:
            theme_color = "#" + color
            root.config(bg = theme_color)
            label.config(bg = theme_color)
            frame1.config(bg = theme_color)
            frame2.config(bg = theme_color)
            label.config(bg = theme_color)
            label2.config(bg = theme_color)
            frame3.config(bg = theme_color)
            but.config(fg = theme_color)
            label3.config(bg = theme_color)
        except:
            label.config(text = "ColorError")
    return

def anime_s_window():
    global awin
    awin = tk.Tk()
    awin.geometry("400x200")
    awin.config(bg = theme_color)
    label = tk.Label(awin, text = "Enjoy watching some animes :)", font = (font1, 15), 
                     bg = theme_color, fg = "white")
    label.pack(pady = 60)
    awin.after(2000, subanime)
    awin.mainloop()
    return

def subanime():
    awin.destroy()
    wb.open("www.9anime.to")
    return

def ipInfo(addr=''):
    from urllib.request import urlopen
    from json import load
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    data = load(res)
    with open("ip.txt", "w") as f:
        for attr in data.keys():
            yo = attr,":",data[attr]
            f.write(str(yo))
    os.startfile("ip.txt")
    return

def phn(number1):  
    import phonenumbers as p
    from phonenumbers import geocoder as g
    from phonenumbers import carrier as c
    from opencage.geocoder import OpenCageGeocode as oo
    key = "0ebdf19437ce4eaf8aba8abf6eee7745"
    number1 = str(number1)
    number = "+" + number1
    p_no = p.parse(number)
    loc = g.description_for_number(p_no, "en")
    s = p.parse(number)
    s_c = c.name_for_number(s, "en")
    gg = oo(key)
    query = str(loc)
    results = gg.geocode(query)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    yo = loc, s_c, lat, lng
    with open("phone.txt", "w") as f:
        f.write(str(yo))
    os.startfile("phone.txt")
    return

def wf():
    import subprocess as s
    import re
    cmdd = s.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
    p = (re.findall("All User Profile     : (.*)\r", cmdd))
    w_lst = []
    if len(p) != 0:
        for name in p:
            wifi_profile = dict()
            p_info = s.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
            if re.search("Security key           : Absent", p_info):
                continue
            else:
                wifi_profile["ssid"] = name
                p_info_pass = s.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
                password = re.search("Key Content            : (.*)\r", p_info_pass)
                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]
                w_lst.append(wifi_profile)
    with open("wifi.txt", "w") as f:
        f.write("Here is the list of all connected wifi's \n \n")
        for i in w_lst:
            f.write(str(i) + '\n')
    os.startfile("wifi.txt")
    return

def sgoogle(search):
    try:
        l = search
        query = " ".join(l[1:]).strip()
        num_ = int(search[0])
        if num_ < 3:
            for i in s(query, num = num_, stop= num_, pause=2):     #tld = 'com',
                wb.open(i)
            root.destroy()
        else:
            label.config(text = "Please do not exceed more than 3 tabs at max")
    except:
        label.config(text = "Error2")
    return

def short_win():
    global button1, swroot, counter, labell
    swroot = tk.Tk()
    swroot.title("Next")
    swroot.config(bg = theme_color)
    labell = tk.Label(swroot, text = "Page 0 / 10", bg = theme_color, fg = "white",
                      font = (font1, 9))
    labell.pack(pady = 15)
    button1 = tk.Button(swroot, text = "Start", fg = theme_color, bg = "white", width = 25,
                        font = (font1, 10), command = next_url)
    button1.pack(pady = 10, padx = 10)
    swroot.attributes("-topmost", True)
    swroot.mainloop()
    return

def next_url():
    try:
        global searching, counter
        a = url_list[counter]
        wb.open(url_list[counter])
        button1.config(text = "Next")
        labell.config(text = f"Page {counter + 1} / 10")
        counter += 1
        if url_list[-1] == a:
            button1.config(text = "That's it!")
    except:
        swroot.destroy()
        searching = False
        counter = 0
    return

def subsearch(l):
    try:
        global url_list, searching, counter
        searching = True
        url_list = []
        query = " ".join(l).strip()
        for i in s(query, tld = "com", num = 10, stop = 10, pause = 2):
            url_list.append(i)
        counter = 0
        short_win()
    except:
        label.config(text = "Error2")
    return

def get5responses():
    global rcounter, lstr, saved
    label2.config(text = f"Please enter {4 - rcounter} more replies")
    tt = ent.get()
    lstr.append(tt)
    ent.delete(0, tk.END)
    rcounter += 1
    if rcounter == 5 or tt == 'ignore':
        user_add(lstr)
    elif tt == "done":
        lstr.pop(-1)
        user_add(lstr)
    return

def user_add(lst):
    d= {}
    d['tag'] = " ".join(text_tobe_written)
    d['patterns'] = " ".join(text_tobe_written)
    d['responses'] = lst
    save_it(d)
    return

def save_it(dictionary):
    lst = a['intents']
    lst.append(dictionary)
    with open(file, "w") as f:
        json.dump(a, f)
    back_to_normal()
    return

def back_to_normal():
    global correcting, rcounter, lstr
    label.config(text = "Saved it in the memory :D")
    label2.config(text = "Type here")
    but.config(text = "Talking to Rem...", state = tk.DISABLED)
    correcting = False
    rcounter = 0
    lstr = []
    return

def talking(word):
    global word_found, text_tobe_written, correcting
    short_memory.append(word)
    word = word.split(" ")
    for i in a['intents']:
        for j in i['patterns']:
            aa = j.lower()
            aa = aa.replace(" ", "oSGFTKREAo")
            bb = ''.join(e for e in aa if e.isalnum())
            cc = bb.replace("oSGFTKREAo", " ")
            dd = l.lemmatize(cc)
            dd = dd.split(" ")
            sim = difflib.SequenceMatcher(None, dd, word).ratio()
            if sim >= 0.90:
                word_found = True
                tag = i['tag']
                respond(tag)
                break
            elif sim > 0.85:
                word_found = True
                tag = i['tag']
                respond(tag)
                break
            elif sim > 0.80:
                word_found = True
                tag = i['tag']
                respond(tag)
                break
            elif sim > 0.75:
                word_found = True
                tag = i['tag']
                respond(tag)
                break
            else:
                continue
    if word_found == False:
        label.config(text = word)
        label2.config(text = "Please enter 5 replies to the it")
        but.config(text = "Answer", state = tk.ACTIVE)
        text_tobe_written = word
        correcting = True
    return

def respond(tag):
    global ans_found
    for i in a['intents']:
        if tag == i['tag']:
            response = i['responses']
            text1 = r.choice(response)
            if text1 != 'ignore':
                if ans_found == False:
                    ans_found = True
                    label.config(text = text1)
                    if i['tag'] != []:
                        label3.config(text = i['tag'])
                    else:
                        label3.config(text = "Unidentifiable")
            else:
                label.config(text = "Unrecognized input")
    return

def short_mem(word):
    global word_found, ans_found
    ans_found = False
    dont_reply = False
    rcntly = len(short_memory)
    lng_ago = 0
    for i in short_memory:
        if word == i:
            frmla = rcntly - lng_ago
            if frmla < 3 :
                label.config(text = "You just wrote that! -_-")
                dont_reply = True
            elif word == max(short_memory, key = short_memory.count):
                if short_memory.count(max(short_memory, key = short_memory.count)) >= 3:
                    label.config(text = "How many times you gon ask that?")
                    dont_reply = True
        else:
            lng_ago += 1
    if dont_reply == False:
        word_found = False
        talking(word)
    return

def develop():
    root.destroy()
    ans = True
    l = []
    z1 = len(a['intents'])
    z2 = 0
    for i in a['intents']:
        print('----------------------------------------------------------------------------')
        if ans == True:
            z2 += 1
            print(i['patterns'])
            print('\n')
            print(f"Tags used so far: {l}")
            print('\n')
            print(f"Previous tag: {i['tag']}")
            print("How would you categorize that?")
            print(f"Tags left: {z1 - z2}")
            user = input("Enter: ").strip().split(" ")
            if user == "":
                continue
            elif user == "-":
                ans = False
                break
            else:
                i['tag'] = " ".join(user)
                for j in user:
                    if j not in l:
                        l.append(j)
        else:
            break
    with open('memory.json', 'w') as f:
        json.dump(a, f)
    return

start()

"""
Assignment!
Identify the chat flow
    create better tags (Started working)
Add memory (stage 1 completed)
Improve answering accuracy (stage 1 completed)
"""