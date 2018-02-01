from tkinter import *
import random 
import time
from PIL import Image
from datetime import datetime
import datetime
from tinydb import TinyDB, Query


root = Tk()
root.geometry("1600x800+0+0")
root.title("Suman_dai_ko_DHOKAN")
root.configure(bg="goldenrod4")


text_Input = StringVar()
operator =""
yes =""
no=""


Tops = Frame(root, width=1600 ,height=50,bg="goldenrod4", relief=RIDGE)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800 ,height=500,bg="goldenrod4",relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height = 700,bg="dark slate blue",relief=SUNKEN)
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
bank_deposite = StringVar()
bank_withdraw = StringVar()
due_amount = StringVar()
order_info = StringVar()
daily_cash = StringVar()
cus_name = StringVar()
cus_no = StringVar()

#++++++++++++++++++++++++++++++++++++++++tinydb example++++++++++++++++++++++
#db = TinyDB("/databse/d4ta.json")
#db.insert({"cus_number":"98938232", "cus_name":"rupen"})

#def no_y():
 #   lis = db.all()
  #  return lis



#===========================================================info===============

lblInfo = Label(Tops, font=("arial",60, "italic bold"),text="Botique Management Systewm",fg="white", bg="dark slate blue", bd=10, anchor="w", relief=RIDGE)
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
    ronley = StringVar()

'''def malware_activate():
    global cmd_active 
    if "rupen" in cmd_active:
        if "rupen" in cmd_active[1]:
            if "ronley" in cmd_active[2]:'''

def ano_win1():
    win1 = Toplevel()
    #this is going to be the window in which there is nothing in the function 
    #of the system on the support in teh main loop
    #there is no limit in the system of teh
    win1.title("this is the owner window:")
    win1.geometry("1600x800+0+0")
    #win1.configure(bg="silver")


    my_info = Frame(win1, width=600, height=700,bg="RoyalBlue4",relief=GROOVE)
    my_info.pack(side=LEFT)
    customer_info = Frame(win1, width=600, height=500,bg="RoyalBlue4", relief=GROOVE)
    customer_info.pack(side=RIGHT)
    
    others_info = Frame(win1, width=100, height=100,bg="RoyalBlue4",relief=GROOVE)
    others_info.pack(side=BOTTOM)


    all_info = Frame(win1, width=50, height=50,bg="RoyalBlue4",relief=RAISED)
    all_info.pack()

    lblname=Label(my_info,font=("arial",20,"italic"),text="Rupen Gurung",bg="powder blue", fg="green", bd=10, relief=SUNKEN).pack(side=TOP)
    lblpro=Label(my_info,font=("arial",  20,"bold"),text="Software Engineer",bg="powder blue", fg="green",bd=10, relief=RAISED).pack()


    win1.mainloop()

btnru = Button(root, font=("arial 20 bold"),bd=20, bg="black",fg="white",text="click",command=ano_win1,relief=GROOVE).pack(side=BOTTOM)



#fucking mazing yr coding
def column(col):
    for coll in col:
        call=cal+1

    return call

def yes_y():
    rupe = Toplevel(root)
    rupe.title("this is second window")
    return

#def no_y():
    #nos = Toplevel(root)
    #nos.title("this is nos window")
    #return


txtDisplay = Entry(f2,font=("arial", 20,"bold"), textvariable=text_Input, bd=30, insertwidth=4,
			   bg="dark slate blue",fg="white", justify="right").grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"), 
	    text="7",bg="dim gray", command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"), 
            text="8",bg="dim gray", command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"), 
            text="9",bg="dim gray", command=lambda: btnClick(9)).grid(row=2,column=2)

#!!!!!!!!!!!!!!!!!!!!!!additions!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Addition=Button(f2,padx=16,pady=16,bd=8,text="+",fg="black",bg="dim gray", command=lambda: btnClick("+")).grid(row=2,column=3)
                                                            
btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"),text="4", bg="dim gray", command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"),text="5", bg="dim gray", command=lambda: btnClick(5)).grid(row=3,column=1)

btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"),text="6",bg="dim gray", command=lambda: btnClick(6)).grid(row=3,column=2)

Subtract=Button(f2,padx=16,pady=16,bd=8,text="-", bg="dim gray", command=lambda: btnClick("-")).grid(row=3,column=3)

btn3=Button(f2,padx=16,pady=16,bd=8,text="3",font=("arial", 20, "bold") ,bg="dim gray", command=lambda: btnClick(3)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,text="2",font=("arial", 20, "bold"), bg="dim gray", command=lambda: btnClick(2)).grid(row=4,column=1)

btn1=Button(f2,padx=16,pady=16,bd=8,text="1",font=("arial", 20, "bold") ,bg="dim gray", command=lambda: btnClick(1)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,text="*", bg="dim gray", command=lambda: btnClick("X")).grid(row=4,column=3)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

btn0=Button(f2,padx=16,pady=16,bd=8,bg="dim gray",text="0",fg="black",font=("arial", 20, "bold"), command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,pady=16,padx=16,bd=8, fg="black",font=("arial", 20, "bold"),text="C",bg="dim gray", command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,fg="black",bd=8,text="=",bg="dim gray", font=("arial", 20,"bold"), command=btnEqualsInput).grid(row=5,column=2)

#btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",text="2",bg="dim gray", command=lambda: btnClick(2)).grid(row=5,column=3)

division=Button(f2,padx=16,pady=16,bd=8,fg="black", text="/", bg="dim gray", command=lambda: btnClick("/")).grid(row=5,column=3)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

rand = StringVar()

#lblReference = Label(f1,font=("arial", 16,"bold"), text="Reference",bd=16,fg="red",bg="red",anchor="w",relief=RIDGE).grid(row=0,column=0)
#txtReference=Entry(f1,font=("arial", 16, "bold"), textvariable=rand, bd=10,insertwidth=4,bg="red",fg="white", justify = "right").grid(row=0,column=1)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
lblReference = Label(f1,font=("arial", 16,"bold"), text="Reference",bd=16,fg="white",bg="green",anchor="w", relief=RIDGE)
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=("arial", 16, "bold"), textvariable=rand, bd=10,insertwidth=4,fg="white",bg="black", justify = "left")
txtReference.grid(row=0,column=1)

#img = "/root/Desktop/Desktop/python/projects/prj1_Botik/1.jpg"
#root.ima = Image.open(img)
#Label (root,bg="white",width=120,height=120, image=ima).pack()

bill_in = StringVar()
bill_out = StringVar()

lblBillIn=Label(f1,font=("arial", 20, "bold"), text="bill_In_no:",bg="powder blue", fg="black",anchor="w",relief=GROOVE).grid(row=1,column=0)
lblBillIn=Entry(f1,font=("arial", 16, "italic"), bd=10, textvariable=bill_in, insertwidth=1,bg="black",fg="white", justify="left").grid(row=2,column=0)


no=Button(root,padx=16,pady=16, font=("arial",12, "bold"),text="no", bd=8,bg="black",command=ano_win1,fg="white",relief=RAISED).pack(side=RIGHT)
yes=Button(root,padx=16,pady=16,font=("arial",12, "bold"),text="yes",bd=8,bg="black", fg="white", command=yes_y,relief=RAISED).pack(side=RIGHT)

lblBillOut=Label(f1,font=("arial",20, "bold"), text="bill_Out_no:", bg="powder blue",fg="black",anchor="w",relief=GROOVE).grid(row=1,column=1)
lblBillOut=Entry(f1,font=("arial",16, "bold"), textvariable=bill_out, insertwidth=1, bd=10,bg="black",fg="white", justify="left").grid(row=2,column=1)


lblbankDepo=Label(f1,font=("arial",16, "bold"), text="Bank_Deposite:",bg="powder blue",fg="black",anchor="w",bd=8,relief=GROOVE).grid(row=1,column=2)
lblbankDepo=Entry(f1,font=("arial",16, "bold"),bg="black",fg="white", textvariable=bank_deposite,insertwidth=1,bd=10,justify="left").grid(row=2,column=2)

lblstock=Label(f1,font=("arial",20, "bold"), text="stock_entry:  ",bg="powder blue",fg="black", anchor="e", relief=GROOVE).grid(row=3,column=0)
lblstock=Entry(f1,font=("arial", 16, "bold"), textvariable=stock_full, insertwidth=1, bd=10,bg="black", fg="white", justify="left").grid(row=4,column=0)

lblstock=Label(f1,font=("arial",16,"bold"),text="shrting mm : ", bg="powder blue", fg="black", anchor="e",relief=GROOVE).grid(row=3, column=1)
lblstock=Entry(f1,font=("arial",16,"bold"),bd=10, textvariable=shrting, bg="black", fg="white", justify="left").grid(row=4, column=1)

lblBankwith=Label(f1, font=("arial", 16, "bold"),fg="black",bg="powder blue",text="bank_withdraw", anchor="e",relief=GROOVE).grid(row=3,column=2)
lblBankwith=Entry(f1,font=("arial",16, "bold"),bd=10, fg="white",bg="black", textvariable=bank_withdraw, insertwidth=1).grid(row=4,column=2)


lblpant=Label(f1, font=("arial", 16, "bold"),text="pant pc:  ", bg="goldenrod4",fg="black",anchor="e").grid(row=5,column=0)
lblpant=Entry(f1, font=("arial", 16, "bold"), bg="black", fg="white", textvariable=pant, insertwidth=1, justify="left",bd=10).grid(row=6,column=0) 

lablsari=Label(f1,font=("arial", 16, "bold"), bg="powder blue",text="sari mm:", fg="black",anchor="e",relief=GROOVE).grid(row=5,column=1)
lablsari=Entry(f1, font=("arial", 16, "bold"), bg="black",bd=10, fg="white",textvariable=sari, insertwidth=1).grid(row=6,column=1)

lblorderinfo=Label(f1,font=("arial", 16, "bold"), bg="powder blue",text="order_info:",fg="black",anchor="e",relief=GROOVE).grid(row=7,column=0)
lblborderinfo=Entry(f1,font=("arial",16, "bold"),bd=8, fg="white",bg="black",textvariable=order_info,insertwidth=1).grid(row=8,column=0)

lblsales =Label(f1, font=("arial", 16, "bold"), bg="powder blue", text="sales_info:", fg="black",anchor="e",relief=GROOVE).grid(row=7,column=1)
lblsales=Entry(f1,font=("arial", 16, "bold"),textvariable=sales, bd=8,fg="white",bg="black",insertwidth=1).grid(row=8,column=1)

lblbuy=Label(f1,font=("arial",16,"bold"),bg="powder blue",text="buy_info:",fg="black",anchor="e",relief=GROOVE).grid(row=9,column=0)
lblbuy=Entry(f1,font=("arial",16,"bold"),insertwidth=1, textvariable=buy,bd=8,fg="white",bg="black").grid(row=10,column=0)

lblcustomer=Label(f1,font=("arial",16,"bold"),bg="powder blue",text="cus_name:",fg="black",anchor="e",relief=GROOVE).grid(row=9,column=1)
lblcustomer=Entry(f1,font=("arial",16, "bold"),bd=8,bg="black",fg="white",insertwidth=1, textvariable=cus_name).grid(row=10,column=1)






    

root.mainloop()
#add1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"), 
            #text="+",bg="powder blue", command=lambda: btnClick("+")).grid(row=3,column=6)


#btn10=Button(f2,padx=16,padx=16, fg="blue", font("arial",5,"bold"),
    	     # text="rupen",bg="powder blue", command=rupen).grid(row=3,column=5)

#def function():
   # pass():
    # pass main():
   # root.mainloop()

#for the revies of the follow in the sorry of the same of the tkinter in the main function of the sollow

#main()

