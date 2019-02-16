from tkinter import *

TEXT = "Contacts.txt"
BACKGROUND_COLOUR = "#E96D63"
COLOUR_BUTTON = "#85C1F5"
COLOUR_TEXT_INPUT = "#F4BA70"
ICON = 'icon.ico'

root = Tk()
root.title('Address Book')
IMAGE = "icon.png"
root.geometry("+300+300")
root.resizable(width=FALSE, height=FALSE)
root.configure(bg = BACKGROUND_COLOUR)
try:
    root.iconbitmap(ICON)
except:
    print("icon is missing")
    ICON = None
    root.iconbitmap(ICON)

TEMP_NAME_VAR = StringVar()
TEMP_PHONE_VAR = StringVar()
TEMP_EMAIL_VAR = StringVar()

EDIT_NAME_VAR = StringVar()
EDIT_PHONE_VAR = StringVar()
EDIT_EMAIL_VAR = StringVar()
SEARCH_VAR = StringVar()


def display():
    reorder()
    with open(TEXT) as f:
        lin = f.read().split("\n")
        lines = (sorted(lin))
        if len(lines) == 1:
            Label(root,bg = BACKGROUND_COLOUR, text="You have no friends. That's very sad.").grid(row = 3, columnspan = 4,sticky="NESW")
        for i in range(1,len(lines)):
            contact = lines[i].split("¬")
            createLabel(contact[0], contact[1], contact[2], i)
        heading()
                
        
def heading():
    Label(root, text="Name",font="Verdana 12 underline",bg = BACKGROUND_COLOUR).grid(row=1, column=0, sticky="W",padx=(5, 0),pady=(5, 5))
    Label(root, text="Phone",font="Verdana 12 underline",bg = BACKGROUND_COLOUR).grid(row=1, column=1, sticky="W",padx=(10, 10),pady=(5, 5))
    Label(root, text="Email",font="Verdana 12 underline",bg = BACKGROUND_COLOUR).grid(row=1, column=2, sticky="W",padx=(0, 10),pady=(5, 5))
    Button(root, text="Add New Person", command=add_window,bg = COLOUR_BUTTON).grid(row=0, column=0, sticky="NESW",padx=(5, 5),pady=(5, 5))
    Entry(root, textvariable=SEARCH_VAR, bg = COLOUR_TEXT_INPUT).grid(row=0, column=1, columnspan=2,sticky="NESW",pady=(5, 5))
    Button(root, text="Search",command = lambda: search(SEARCH_VAR),bg = COLOUR_BUTTON).grid(row=0, column=3, sticky="NESW",padx=(5, 5),pady=(5, 5))


def createLabel(name, phone, email, i):
    Label(root, text=name,bg = BACKGROUND_COLOUR).grid(row=i + 2, column=0, sticky="W",padx=(5, 0),pady=(5, 5))
    Label(root, text=phone,bg = BACKGROUND_COLOUR).grid(row=i + 2, column=1, sticky="W",padx=(10, 10),pady=(5, 5))
    Label(root, text=email,bg = BACKGROUND_COLOUR).grid(row=i + 2, column=2, sticky="W",padx=(0, 10),pady=(5, 5))
    Button(root, text="Edit", command=lambda: edit_person_window(i-1),bg = COLOUR_BUTTON).grid(row=i + 2, column=3, sticky="EW",padx=(5, 5))


def add_window():
    addwindow = Toplevel(root)
    addwindow.configure(background=BACKGROUND_COLOUR)
    menubar = Menu(addwindow)
    menubar.add_command(label="Quit", command=quit)
    addwindow.config(menu=menubar)
    addwindow.title('Add Person')
    root.resizable(width=FALSE, height=FALSE)
    addwindow.geometry("+300+300")
    Label(addwindow, text="Name",bg = BACKGROUND_COLOUR).grid(row=0, sticky="W",padx=(5, 5),pady=(5, 0))
    Label(addwindow, text="Phone",bg = BACKGROUND_COLOUR).grid(row=1, sticky="W",padx=(5, 5),pady=(5, 5))
    Label(addwindow, text="Email",bg = BACKGROUND_COLOUR).grid(row=2, sticky="W",padx=(5, 5),pady=(0, 5))
    Entry(addwindow, textvariable=TEMP_NAME_VAR, bg = COLOUR_TEXT_INPUT).grid(row=0, column=1,sticky="NESW",padx=(5, 5),pady=(5, 0))
    Entry(addwindow, textvariable=TEMP_PHONE_VAR, bg = COLOUR_TEXT_INPUT).grid(row=1, column=1,sticky="NESW",padx=(5, 5),pady=(5, 5))
    Entry(addwindow, textvariable=TEMP_EMAIL_VAR, bg = COLOUR_TEXT_INPUT).grid(row=2, column=1,sticky="NESW",padx=(5, 5),pady=(0, 5))
    Button(addwindow, text="Enter", command=enter_data,bg = COLOUR_BUTTON).grid(row=4, column=1, sticky="NESW",padx=(5, 5),pady=(0, 5))
    Button(addwindow, text="Back", command=addwindow.destroy,bg = COLOUR_BUTTON).grid(row=4, column=0, sticky="NESW",padx=(5, 0),pady=(0, 5))
    addwindow.iconbitmap(ICON)
    

def enter_data():
    if TEMP_NAME_VAR.get() == "" and TEMP_PHONE_VAR.get() == "" and TEMP_EMAIL_VAR.get() == "":
        return None
    try:
        with open(TEXT, "a") as file:
            file.write(TEMP_NAME_VAR.get().title() + "¬" + TEMP_PHONE_VAR.get() + "¬" + TEMP_EMAIL_VAR.get() + "\n")
    except:
        pass
    else:
        TEMP_NAME_VAR.set("")
        TEMP_PHONE_VAR.set("")
        TEMP_EMAIL_VAR.set("")
        clear()
        display()


def clear():
    liste = root.grid_slaves()
    for l in liste:
        l.destroy()


def search(qq):
    if len(qq.get()) == 0:
        clear()
        display()
        return None
    NAMES = []
    PHONES = []
    EMAILS = []
    FOUND_ARRAY = []
    file = open(TEXT,"r")
    person_list = file.read().split("\n")
    try:
        for contact in person_list:
            n,p,e = contact.split("¬")
            NAMES.append(n.lower())
            PHONES.append(p.lower())
            EMAILS.append(e.lower())       
    except:
        for name in NAMES:
            if name.find(qq.get().lower()) != -1:
                num_var = NAMES.index(name)
                FOUND_ARRAY.append(num_var)
                NAMES.pop(num_var)
                NAMES.insert(num_var,"")
        for phone_numbers in PHONES:
            if phone_numbers.find(qq.get().lower()) != -1:
                num_var = PHONES.index(phone_numbers)
                FOUND_ARRAY.append(num_var)
                PHONES.pop(num_var)
                PHONES.insert(num_var,"")
        for email in EMAILS:
            if email.find(qq.get().lower()) != -1:
                num_var = EMAILS.index(email)
                FOUND_ARRAY.append(num_var)
                EMAILS.pop(num_var)
                EMAILS.insert(num_var,"")
        FOUND_ARRAY = (list(dict.fromkeys(FOUND_ARRAY)))
        clear()
        file = open(TEXT,"r")
        lines = file.read().split("\n")
        for i in FOUND_ARRAY:
            contact = lines[i].split("¬")
            createLabel(contact[0], contact[1], contact[2], i)
        heading()

        

def edit_person_window(i):
    with open(TEXT) as f:
        lines = f.read()
    editwindow = Toplevel(root)
    editwindow.configure(background=BACKGROUND_COLOUR)
    menubar = Menu(editwindow)
    menubar.add_command(label="Quit", command=quit)
    editwindow.config(menu=menubar)
    editwindow.geometry("+300+300")
    editwindow.title('Edit Person')
    editwindow.resizable(width=FALSE, height=FALSE)
    person = lines.split("\n")
    person_i_want = person[i].split("¬")
    EDIT_NAME_VAR.set(person_i_want[0])
    EDIT_PHONE_VAR.set(person_i_want[1])
    EDIT_EMAIL_VAR.set(person_i_want[2])
    Label(editwindow, text="Name",bg = BACKGROUND_COLOUR).grid(row=0, sticky="W",padx=(5, 5),pady=(5, 0))
    Label(editwindow, text="Phone",bg = BACKGROUND_COLOUR).grid(row=1, sticky="W",padx=(5, 5),pady=(5, 5))
    Label(editwindow, text="Email",bg = BACKGROUND_COLOUR).grid(row=2, sticky="W",padx=(5, 5),pady=(0, 5))
    Entry(editwindow, textvariable=EDIT_NAME_VAR, bg = COLOUR_TEXT_INPUT).grid(row=0, column=1,sticky="NESW",columnspan = 2,padx=(5, 5),pady=(5, 0))
    Entry(editwindow, textvariable=EDIT_PHONE_VAR, bg = COLOUR_TEXT_INPUT).grid(row=1, column=1,sticky="NESW",columnspan = 2,padx=(5, 5),pady=(5, 5))
    Entry(editwindow, textvariable=EDIT_EMAIL_VAR, bg = COLOUR_TEXT_INPUT).grid(row=2, column=1,sticky="NESW",columnspan = 2,padx=(5, 5),pady=(0, 5))
    Button(editwindow, text="Save", command=lambda: edit_person(EDIT_NAME_VAR, EDIT_PHONE_VAR, EDIT_EMAIL_VAR, i, person, editwindow),bg = COLOUR_BUTTON).grid(pady=(0, 5),row=4, column=1, sticky="NESW",padx=(5, 5))
    Button(editwindow, text="Back", command=editwindow.destroy,bg = COLOUR_BUTTON).grid(row=4, column=0, sticky="NESW",padx=(5, 0),pady=(0, 5))
    Button(editwindow, text="Del", command=lambda: del_person(i, person, editwindow),bg = COLOUR_BUTTON).grid(row=4, column=2,sticky="NESW",padx=(0, 5),pady=(0, 5))
    editwindow.iconbitmap(ICON)

def del_person(i, person, window):
    person.pop(i)
    re_write(i, person, window)


def edit_person(name, phone, email, i, person, window):
    if name.get() == "" and phone.get() == "" and email.get() == "":
        return None
    person.pop(i)
    person.insert(i, name.get() + "¬" + phone.get() + "¬" + email.get())
    re_write(i, person, window)


def re_write(i, person, window):
    file = open(TEXT,"w")
    for i in range(0,len(person)-1):
        file.write(person[i])
        file.write("\n")
    file.close()
    clear()
    display()
    window.destroy()


def about():
    about_window = Toplevel(root)
    about_window.configure(background=BACKGROUND_COLOUR)
    about_window.geometry("+300+300")
    about_window.title('About')
    about_window.iconbitmap(ICON)
    Label(about_window, text="www.allofthemaths.com",bg = BACKGROUND_COLOUR).grid()


def reorder():
    file = open(TEXT,"r")
    lines = file.read().split("\n")
    lines = (sorted(lines))
    file.close()
    file = open(TEXT,"w")
    for i in range(1,len(lines)):
        file.write(lines[i])
        file.write("\n")
    file.close()

    
def tryfile():
    try:
        file = open(TEXT,"r")
        file.close()
    except:
        file = open(TEXT,"w")
        file.close()

menubar = Menu(root)
menubar.add_command(label="Quit", command=quit)
menubar.add_command(label="About", command= about)
root.config(menu=menubar)

tryfile()
display()
mainloop()
