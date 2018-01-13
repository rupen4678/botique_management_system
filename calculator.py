from tkinter import *
import random 
import time
from PIL import Image
from datetime import datetime
import datetime

root = Tk()
root.geometry("1600x800+0+0")
root.title("Suman_dai_ko_DHOKAN")
#root.configure(bg="white")


text_Input = StringVar()
operator =""
yes =""
no=""


Tops = Frame(root, width=1600 ,height=50,bg="powder blue", relief=RIDGE)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800 ,height=500,bg="powder blue",relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height = 700,bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)

#f3= Frame(root,width=1600,height=300,fg="blue", bg="powder blue", relief=SUNKEN).pack(side=Bottom)



#==========================================================Time=======================================
localtime=time.asctime(time.localtime(time.time()))

#datetime=Label(Tops,font("arial",20,"bold"),text=nowTime,bd=10 ,bg="black", fg="white", anchor="w").pack()
#++++++++++++++++++++++++++++++Varibales_inset+++++++++++++++++++++++++++++++++

order_bef = StringVar()
stock_full = StringVar()
shrting = StringVar()
pant = StringVar()
sari = StringVar()
order_info = StringVar()
delivery_report = StringVar()
daily_info = StringVar()
sales = StringVar()
buy = StringVar()
total_bank = StringVar()
deposite = StringVar()
withdraw = StringVar()
due_amount = StringVar()
order_info = StringVar()
daily_cash = StringVar()

#===========================================================info===============

lblInfo = Label(Tops, font=("arial",60, "italic bold"),text="Botique Management System",fg="white", bg="black", bd=10, anchor="w", relief=RIDGE)
lblInfo.pack()
lblInfo = Label(Tops, font=("arial",30, "bold"),text=localtime,fg="white",bg="black", bd=10, anchor="w", relief=RIDGE)
lblInfo.pack()

#===========================================================Calculator================================== 
"""def current_dir():
    import os
    import sys

    DIR = os.getcwd()
    print(DIR)
lblInfo = Label(Tops, font=("arial",60, "italic"),text=current_dir,fg="black",bg="powder blue",bd=10, anchor="W")
lblInfo.pack()

    #DIR = dir
    #return dir
    """

#randomBtn=Button(f1,pady=16,padx=16,bd=8,bg="powder blue", text="C_dir", command=lambda: current_dir(dir)).pack(side=TOP)


def btnClick(numbers):
    global operator 
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput(): 
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

def bill_entry():
    global bill_in
    global bill_out
    bill_out = ""
    bill_in = ""


def rupen():
    global rupen
    rupen = rupen

#fucking mazing yr coding
def column(col):
    for coll in col:
        call=cal+1

    return call

def yes_y():
    rupe = Toplevel(root)
    rupe.title("this is second window")
    return rupe


txtDisplay = Entry(f2,font=("arial", 20,"bold"), textvariable=text_Input, bd=30, insertwidth=4,
			   bg="powder blue", justify="right").grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"), 
	    text="7",bg="powder blue", command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"), 
            text="8",bg="powder blue", command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"), 
            text="9",bg="powder blue", command=lambda: btnClick(9)).grid(row=2,column=2)

#!!!!!!!!!!!!!!!!!!!!!!additions!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Addition=Button(f2,padx=16,pady=16,bd=8,text="+",fg="black",bg="powder blue", command=lambda: btnClick("+")).grid(row=2,column=3)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"),text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"),text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3,column=1)

btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"),text="6",bg="powder blue", command=lambda: btnClick(6)).grid(row=3,column=2)

Subtract=Button(f2,padx=16,pady=16,bd=8,text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3,column=3)

btn3=Button(f2,padx=16,pady=16,bd=8,text="3",font=("arial", 20, "bold") ,bg="powder blue", command=lambda: btnClick(3)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,text="2",font=("arial", 20, "bold"), bg="powder blue", command=lambda: btnClick(2)).grid(row=4,column=1)

btn1=Button(f2,padx=16,pady=16,bd=8,text="1",font=("arial", 20, "bold") ,bg="powder blue", command=lambda: btnClick(1)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,text="*", bg="powder blue", command=lambda: btnClick("X")).grid(row=4,column=3)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

btn0=Button(f2,padx=16,pady=16,bd=8,bg="powder blue",text="0",fg="black",font=("arial", 20, "bold"), command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,pady=16,padx=16,bd=8, fg="black",font=("arial", 20, "bold"),text="C",bg="powder blue", command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,fg="black",bd=8,text="=",bg="powder blue", font=("arial", 20,"bold"), command=btnEqualsInput).grid(row=5,column=2)

#btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",text="2",bg="powder blue", command=lambda: btnClick(2)).grid(row=5,column=3)

division=Button(f2,padx=16,pady=16,bd=8,fg="black", text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5,column=3)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

rand = StringVar()

lblReference = Label(f1,font=("arial", 16,"bold"), text="Reference",bd=16,fg="black",anchor="w",relief=GROOVE)
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=("arial", 16, "bold"), textvariable=rand, bd=10,insertwidth=4,bg="powder blue", justify = "right")
txtReference.grid(row=0,column=1)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
lblReference = Label(f1,font=("arial", 16,"bold"), text="Reference",bd=16,fg="black",anchor="w", relief=GROOVE)
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=("arial", 16, "bold"), textvariable=rand, bd=10,insertwidth=4,bg="powder blue", justify = "right")
txtReference.grid(row=0,column=1)

#img = "/root/Desktop/Desktop/python/projects/prj1_Botik/1.jpg"
#root.ima = Image.open(img)
#Label (root,bg="white",width=120,height=120, image=ima).pack()

bill_in = StringVar()
bill_out = StringVar()

lblBillIn=Label(f1,font=("arial", 20, "bold"), text="bill_In_no:",bg="white", fg="black",anchor="w",relief=GROOVE).grid(row=1,column=0)
lblBillIn=Entry(f1,font=("arial", 16, "italic"), bd=10, textvariable=bill_in, insertwidth=1,bg="black",fg="powder blue", justify="left").grid(row=2,column=0)

no=Button(root,padx=16,pady=16, font=("arial",12, "bold"),text="no", bd=8,bg="black", fg="white",relief=RAISED).pack(side=RIGHT)
yes=Button(root,padx=16,pady=16,font=("arial",12, "bold"),text="yes",bd=8,bg="black", fg="white", command=yes_y,relief=RAISED).pack(side=RIGHT)

lblBillOut=Label(f1,font=("arial",20, "bold"), text="bill_Out_no:", bg="white",fg="black",anchor="w",relief=GROOVE).grid(row=1,column=1)
lblBillOut=Entry(f1,font=("arial",16, "bold"), textvariable=bill_out, insertwidth=1, bd=10,bg="black",fg="green", justify="left").grid(row=2,column=1)

lblstock=Label(f1,font=("arial",20, "bold"), text="stock_entry:  ",bg="white",fg="black", anchor="e", relief=GROOVE).grid(row=3,column=0)
lblstock=Entry(f1,font=("arial", 16, "bold"), textvariable=stock_full, insertwidth=1, bd=10,bg="black", fg="green", justify="left").grid(row=4,column=0)

lblstock=Label(f1,font=("arial",16,"bold"),text="shrting mm : ", bg="white", fg="black", anchor="e").grid(row=3, column=1)
lblstock=Entry(f1,font=("arial",16,"bold"),bd=10, textvariable=shrting, bg="black", fg="green", justify="left").grid(row=4, column=1)
lblpant=Label(f1, font=("arial", 16, "bold"), bg="white",fg="white", text="pant pcs: ",anchor="e", relief=GROOVE).grid(row=5,column=0)
lblpant=Entry(f1, font=("arial", 16, "bold"), bg="black", fg="green", textvariable=pant, insertwidth=1, justify="left",bd=10).grid(row=6,column=0)



root.mainloop()
#add1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"), 
            #text="+",bg="powder blue", command=lambda: btnClick("+")).grid(row=3,column=6)


#btn10=Button(f2,padx=16,padx=16, fg="blue", font("arial",5,"bold"),
    	     # text="rupen",bg="powder blue", command=rupen).grid(row=3,column=5)

#def function():
   # pass():
    # pass main():
   # root.mainloop()

#main()

