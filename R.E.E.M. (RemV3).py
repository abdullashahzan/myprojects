import random, json, pickle, nltk, pyjokes, difflib, os
import numpy as np
from nltk.stem import WordNetLemmatizer as wnl
from tensorflow.keras.models import load_model
import tkinter as tk
import random as rrr
import webbrowser as wb
from googlesearch import search as s
from PIL import ImageTk, Image

words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))
model = load_model("rem.h5")
theme_color = "#003d66"
font1 = "Microsoft YaHei Light"
login = False
file = "memory.json"
a = json.loads(open(file).read())
l = wnl()
lstr = []
short_memory = []
jox = []
word_found = False
formula = 0
correcting = False
searching = False
counter = 0
rcounter = 0
ans_found = False
saved = False
signin = False

def load():
    import cv2
    import tkinter as tk
    from PIL import Image, ImageTk
    window = tk.Tk()
    window.wm_title("Rem")
    window.geometry("644x354")
    window.config(bg = theme_color)
    imageFrame = tk.Frame(window, width=640, height=350)
    imageFrame.grid(row=0, column=0)
    lmain = tk.Label(imageFrame)
    lmain.grid(row=0, column=0)
    cap = cv2.VideoCapture('remLoadScreen.mp4')
    def show_frame():
        try:
            _, frame = cap.read()
            resize = cv2.resize(frame, (640, 350), interpolation = cv2.INTER_LINEAR)
            cv2image = cv2.cvtColor(resize, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame) 
        except:
            window.destroy()
    sliderFrame = tk.Frame(window, width=600, height=100)
    sliderFrame.grid(row = 600, column=0)
    show_frame()
    window.attributes("-topmost", True)
    window.protocol("WM_DELETE_WINDOW", dontclose)
    window.mainloop()
    start()
    return

def load2():
    global rrroot
    rrroot = tk.Tk()
    img = ImageTk.PhotoImage(Image.open("REM.jpg"))
    panel = tk.Label(rrroot, image = img)
    panel.pack()
    rrroot.attributes("-topmost", True)
    rrroot.protocol("WM_DELETE_WINDOW", dontclose)
    rrroot.after(1500, start)
    rrroot.mainloop()
    return

def dontclose():
    pass

def start():
    global ent, label, root, frame1, frame2, label2, frame3, but
    root = tk.Tk()
    root.geometry("700x350")
    root.title("REEM")
    root.config(bg = theme_color)
    frame1 = tk.Frame(root, bg = theme_color)
    frame1.pack()
    frame2 = tk.Frame(root, bg = theme_color)
    frame2.pack()
    frame3 = tk.Frame(root, bg = theme_color)
    frame3.pack()
    label = tk.Label(frame1, text = "Reem at your service!!", 
                     font = (font1, 15), bg = theme_color, fg = 'white',
                     width = 64, height = 5)
    label.pack(pady = 5)
    label2 = tk.Label(frame2, text = "Type here: ", font = (font1, 11), bg = theme_color, fg = 'white')
    label2.pack()
    ent = tk.Entry(frame2, font = (font1, 10), width = 70)
    ent.pack()
    but = tk.Button(frame3, text = "Talking to Reem...", font = (font1, 14), fg = theme_color,
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
    chng_color("#003d66")
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
        elif listcc[1] == "shortcut":
            shortcutpanel()
        elif listcc[1] == "train" and listcc[2] == "model":
            root.destroy()
            train_model()
        else:
            label.config(text = "Error")
    except:
        label.config(text = "Error1")
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

def shortcutpanel():
    global labelga, buttt1, buttt2, troot
    troot = tk.Tk()
    troot.title("REM")
    troot.config(bg = theme_color)
    labelframe = tk.Frame(troot, bg = theme_color)
    labelframe.grid(row = 0, column = 0)
    butframe = tk.Frame(troot, bg = theme_color)
    butframe.grid(row = 1, column = 0)
    labelga = tk.Label(labelframe, text = "Quick setup tools", bg = theme_color, fg = "white",
                     font = (font1, 15))
    labelga.pack(pady = 15)
    buttt1 = tk.Button(butframe, text = "Mom's setup", width = 25, height = 5, fg = theme_color,
                     bg = "white", font = (font1, 12), command = mom)
    buttt1.grid(row = 0, column = 0, padx = 5, pady = 10)
    buttt2 = tk.Button(butframe, text = "Quran", width = 25, height = 5, 
                     fg = theme_color, bg = "white", font = (font1, 12), command = quran)
    buttt2.grid(row = 0, column = 1, padx = 5, pady = 10)
    troot.attributes("-topmost", True)
    troot.mainloop()
    return

def mom():
    buttt1.config(state = tk.DISABLED)
    buttt2.config(state = tk.DISABLED)
    labelga.config(text = "Setting up mom's setup!")
    wb.open("https://web.whatsapp.com/")
    wb.open_new_tab("https://me.classera.com/teacher#networkfirst")
    os.startfile("Zoom")
    troot.destroy()
    root.destroy()
    return

def quran():
    buttt1.config(state = tk.DISABLED)
    buttt2.config(state = tk.DISABLED)
    labelga.config(text = "Starting reasearch program!")
    wb.open("www.google.com")
    wb.open("https://quran.com/")
    troot.destroy()
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
    d['tag'] = "".join(text_tobe_written)
    d['patterns'] = ["".join(text_tobe_written)]
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

def clean_sentence(sentence):
    sentence = sentence.strip().lower().replace(" ", "#")
    sentence = ''.join(e for e in sentence if e.isalnum() or e == "#")
    sentence = sentence.replace("#", " ").split(" ")
    sentence_words = [l.lemmatize(wordd) for wordd in sentence]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict(sentence):
    global error_threshold, prob
    bagofwords = bag_of_words(sentence)
    result = model.predict(np.array([bagofwords]))[0]
    error_threshold = 0.95
    rresult = [[i, r] for i, r in enumerate(result) if r > error_threshold]
    rresult.sort(key = lambda x: x[1], reverse=True)
    return_list = []
    for r in rresult:
        return_list.append({'intent': classes[r[0]], 'probability':str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
        else:
            result = "Couldnt find answer"
    return result

def vocabulary(word):
    global theme_color, login, signin
    if word == "1439":
        theme_color = "#800020"
        label.config(text = "Please type in password to enable administrator tools")
        but.config(text = 'BACK', state = tk.ACTIVE)
        signin = True
        # login = True
        # chng_color("#800020")
    elif signin == True and word == "iloveallah123":
        login = True
        chng_color("#800020")
        label.config(text = "Welcome!")
        but.config(text = 'Log out', state = tk.ACTIVE)
        signin = False
    elif word == "close yourself":
        root.destroy()
    elif word == "please tell me a joke":
        while True:
            joke = pyjokes.get_joke(language = "en", category= "neutral")
            if joke not in jox:
                jox.append(joke)
                te(joke)
                break
            if joke in jox:
                continue
            else:
                break
    elif difflib.SequenceMatcher(None, word, "how old are you").ratio() > 0.95:
        label.config(text = "65")
    elif word.split(" ")[0] == "color":
        chng_color(word.split(" ")[1])
    else:
        short_mem(word)
    return

def talking(word):
    short_memory.append(word)
    wf = False
    try:
        ints = predict(word)
        res = get_response(ints, a)
        if res != "ignore":
            te(res)
        else:
            label.config(text = "Error text")
    except:
        for i in a['intents']:
            for j in i['patterns']:
                sim = difflib.SequenceMatcher(None, j, word).ratio()
                if sim > 0.85:
                    respond(i['tag'])
                    wf = True
                    break
                elif sim > 0.80:
                    respond(i['tag'])
                    wf = True
                    break
                elif sim > 0.75:
                    wf = True
                    tag = i['tag']
                    respond(tag)
                    break
                elif sim > 0.70:
                    wf = True
                    tag = i['tag']
                    respond(tag)
                    break
                else:
                    continue
        if wf == False:
            global text_tobe_written, correcting
            label.config(text = word)
            label2.config(text = "Please enter 5 replies to the it")
            but.config(text = "Answer", state = tk.ACTIVE)
            text_tobe_written = word
            correcting = True
    return

def respond(tag):
    for i in a['intents']:
        if tag == i['tag']:
            response = i['responses']
            if len(response) != 0:
                text1 = rrr.choice(response)
                if text1 != 'ignore':
                    te(text1)
                else:
                    label.config(text = "Unrecognized input")
    return

def short_mem(word):
    dont_reply = False
    rcntly = len(short_memory)
    lng_ago = 0
    for i in short_memory:
        if word == i:
            frmla = rcntly - lng_ago
            if frmla < 3 :
                label.config(text = "I don't like to reply twice for the same question")
                dont_reply = True
            elif word == max(short_memory, key = short_memory.count):
                if short_memory.count(max(short_memory, key = short_memory.count)) >= 2:
                    label.config(text = "How many times you gon ask that?")
                    dont_reply = True
        else:
            lng_ago += 1
    if dont_reply == False:
        talking(word)
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
        except:
            label.config(text = "ColorError")
    return

def develop():
    root.destroy()
    savecon = True
    final_list = []
    for i in a['intents']:
        if len(i['patterns']) <= 1:
            print(i['patterns'])
            print(i['responses'])
            user = input("Enter?")
            if user == "":
                d = {}
                d['tag'] = " ".join(i['patterns'])
                d['patterns'] = i['patterns']
                d['responses'] = i['responses']
                final_list.append(d)
            elif user == "-":
                print("Files wont be saved!")
                savecon = False
                break
            else:
                continue
    if savecon == True:
        dd = {}
        dd['intents'] = final_list
        with open("memory.json", "w") as f:
            json.dump(dd, f)
    return

def te(answerr):
    answer = answerr
    wl = answer.split(" ")
    for i in range(len(wl)):
        if i == 8 or i == 18:
            wl.insert(i, "\n")
    kk = " ".join(wl)
    label.config(text = kk.strip())
    return

def train_model():
    global but, ent #, label
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Activation, Dropout
    from tensorflow.keras.optimizers import SGD
    
    lemmatizer = wnl()
    file = "memory.json"
    a = json.loads(open(file).read())
    
    words, classes, documents, ignore_letters = [], [], [], ['?', ".", "!", ","]
    
    for i in a['intents']:
        for j in i['patterns']:
            a = j.replace(" ", "#")
            b = ''.join(e for e in a if e.isalnum() or e == "#").replace("#", " ")
            word_list = nltk.word_tokenize(b)
            words.extend(word_list)
            documents.append((word_list, i['tag']))
            if i['tag'] not in classes:
                classes.append(i['tag'])
    
    """
    Notes:
    Documents = [ (['hello', 'how', 'are', 'you'], greetings), (['bye', 'bye'], goodbye) ]
    Documents contain list of tuples which contain the sentence in the form of list and its tag
    
    classes = ['greetings', 'goodbye', 'health']
    Classes contain all the tags which are saved in the json file
    """
    
    words = [lemmatizer.lemmatize(aaa.lower()) for aaa in words]
    words = sorted(set(words))
    classes = sorted(set(classes))
    
    pickle.dump(words, open('words.pkl', 'wb'))
    pickle.dump(classes, open('classes.pkl', 'wb'))
    
    training, output_empty = [], [0] * len(classes)
    
    for k in documents:
        bag = []
        questions = k[0]
        questions = [lemmatizer.lemmatize(kkk.lower()) for kkk in questions]
        for l in words:
            if l in questions:
                bag.append(1)
            else:
                bag.append(0)
        
        output_row = list(output_empty)
        output_row[classes.index(k[1])] = 1
        training.append([bag, output_row])
    
    random.shuffle(training)
    training = np.array(training)
    
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])
    
    #Neural networks start from here
    
    model = Sequential()
    model.add(Dense(256, input_shape = (len(train_x[0]),), activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation = 'softmax'))
    
    sgd = SGD(lr = 0.01, decay = 1e-6, momentum=0.9, nesterov=True)
    model.compile(loss = 'categorical_crossentropy', optimizer = sgd, metrics=['accuracy'])
    hist =  model.fit(np.array(train_x), np.array(train_y), epochs = 1000, batch_size= 10, verbose=1)
    model.save('rem.h5', hist)

start()        
 
