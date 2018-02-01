

try:
    import tkinter as tk
    from tkinter import messagebox
    print("running in python3")
except ImportError:
    print("runnning in python2.7")
    import Tkinter as tk
    # from http://effbot.org/tkinterbook/entry.htm
from tkinter import *

failure_max = 3
passwords = [('root', 'toor'), ('suman', 'password')]
def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry
def enter(event):
    check_password()

def window2_init():

    root = Tk()
    #win2 = TopLevel()
    root.title("main window")
    llb1 = Label(root,text="hello this will be main window").pack()
    btn1 = Button(root,font("arial", 20, "italic"), padx=16,pady=16, bg="black"                                 ,fg="white",relief="RAISED").pack()

    root.mainloop()

def check_password(failures=[]):
    """ Collect 1's for every failure and quit program in case of failure_max failures """
    print(user.get(), password.get())
    if (user.get(), password.get()) in passwords:
        root.destroy()
        #messagebox.showinfo('Logged in')
        window2_init()
        return
    failures.append(1)
    if sum(failures) >= failure_max:
        root.destroy()
        raise SystemExit('Unauthorized login attempt')
    else:
        root.title('Try again. Attempt %i/%i' % (sum(failures)+1, failure_max))
        
root = tk.Tk()
root.geometry('300x160')
root.title('Enter your information')
    #frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
    #entrys with not shown text
user = make_entry(parent, "User name:", 16)
password = make_entry(parent, "Password:", 16, show="*")
    #button to attempt to login
b = tk.Button(parent, borderwidth=4, text="Login", width=10, pady=8, command=check_password)
b.pack(side=tk.BOTTOM)
password.bind('<Return>', enter)
user.focus_set()
parent.mainloop()

