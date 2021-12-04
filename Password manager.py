from tkinter import *
import requests
import time
import tkinter.messagebox as tmsg
from tkinter import ttk
def home():
    global start
    start = Tk()
    start.title("Password Manager")
    start.configure()
    start.geometry("720x400")
    start.minsize(720, 400)
    maxwidth = start.winfo_screenwidth()
    maxheight = start.winfo_screenheight()
    frame = Frame(start, bg="grey")
    
    start.maxsize(maxwidth, maxheight)
    logo = Frame(start, bg="grey", borderwidth=2)
    logo.pack(side=TOP, fill=X)
    logotext = Label(logo, text="Welcome to Password Manager", fg="green",
                     font="vardana 15 bold", bg="lightblue")
    logotext.pack(fill=X)
    
    space1 = Label(start, text="")
    space1.pack()
    space3 = Label(start, text="")
    space3.pack()
    space2 = Label(start, text="")
    space2.pack()
    separator = ttk.Separator(start, orient='horizontal')
    separator.pack(side='top', fill='x')
    getpasswordbutton = Button(start, text="Save Password", bg="lightblue", font="vardana 20 bold", fg="black", command=savetasks)
    getpasswordbutton.pack(padx=10, pady=10,ipadx=60, ipady=10)

    
    separator = ttk.Separator(start, orient='horizontal')
    separator.pack(side='top', fill='x')
    enterpasswordbutton = Button(start, text="Show Saved Passwords", bg="lightblue", font="vardana 20 bold", fg="black",activeforeground='red', activebackground='blue',
                                 command=showtasks)
    enterpasswordbutton.pack(padx=10, pady=10, ipady=10 )
   
    separator = ttk.Separator(start, orient='horizontal')
    separator.pack(side='top', fill='x')
    deletepasswordbutton = Button(start, text="Delete All Passwords", bg="orange", font="vardana 20 bold", fg="black",
                                 command=deleteall)
    deletepasswordbutton.pack(padx=10, pady=10, ipady=10,ipadx=20)
    start.mainloop()
def deleteall():
    
    a=tmsg.askquestion("Verify!","Are you sure you want to delete all your saved Passwords?")
    if a=="yes":
        url = "http://143.198.247.74:8080/passwords/delete"
        r=requests.post(url)
        print(r.text)
def savetasks():

    global savetaskscreen
    savetaskscreen= Tk()
    savetaskscreen.title("Save Password")
    savetaskscreen.geometry("720x400")

    r1 = Frame(savetaskscreen)
    r1.pack(fill=Y)
    logo = Label(r1, text="Enter Password to Save ", fg="black", font="verdana 22 bold",
                 bg="lightblue")
    logo.pack(fill=X)
    logo1 = Label(r1, text="")
    logo1.pack()

    n2 = Label(r1, text="Enter Password Source: ")
    n2.pack()
    def submittask():
        url = "http://143.198.247.74:8080/enterpassword"
        name=femailenrty.get()
        task=femailenrty2.get()
        data={"name":name,"password":task}
        r=requests.post(url,json=data)

        a.config(text="Password saved successfully.",fg="green")

    femailidt1 = StringVar()

    femailenrty = Entry(r1, textvariable=femailidt1, font="vardana 20")

    femailenrty.pack(fill=X, pady=20)
    n21 = Label(r1, text="Enter Password: ")
    n21.pack()
    femailidt12 = StringVar()

    femailenrty2 = Entry(r1, textvariable=femailidt12, font="vardana 20")

    femailenrty2.pack(fill=X, pady=20)
    submitcode = Button(r1, text="Save Passwords", font="vardana 20 bold", bg="#98DBC6", fg="black",
                        command=submittask)
    submitcode.pack(pady=20)
    a=Label(r1,text="Enter Password details and click save",font="vardana 15 ")
    a.pack()
    savetaskscreen.mainloop()


def showtasks():
    global showtask
    showtask = Tk()
    showtask.title("Show Passwords")
    showtask.geometry("720x400")

    r1 = Frame(showtask)
    r1.pack(fill=Y)
    logo = Label(r1, text="Click on Any Name to delete that Password: ", fg="black", font="verdana 15 bold",
                 bg="lightblue")
    logo.pack(fill=X)
    logo1 = Label(r1, text="")
    logo1.pack()

    url = "http://143.198.247.74:8080/allpasswords"
    r=requests.get(url)
    a=r.json()
    print(a)
    def clicked(event):
        x = mylist.curselection()
        x2 = mylist.get(x)

        for key, value in a.items():
            for i in value:
              if i["name"]==x2:
                  
                  url="http://143.198.247.74:8080/password/"+i["id"]
                  r=requests.delete(url)

                  tmsg.showinfo("Deleted!","Password has been deleted!")
                  showtask.destroy()
                  start.destroy()
                  home()

    sb = Scrollbar(showtask)
    sb.pack(side=RIGHT, fill=Y)
    mylist = Listbox(showtask, width=300, height=300, yscrollcommand=sb.set, bg="lightgrey", font="helvetica 12 bold"
                     , fg="green")
    
    for key,value in a.items():
        for i in value:
            mylist.insert(END, i["password"])
           
    mylist.pack(side=LEFT, fill=X)
    mylist.bind("<<ListboxSelect>>", clicked)
    sb.config(command=mylist.yview())
if __name__ == '__main__':
    home()

