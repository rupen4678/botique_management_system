from tkinter import *
import random
import time
from PIL import Image
from datetime import datetime
from tinydb import *
import os
import pickle
#from database1 import *
from random import randint

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

#datetime=Label(Tops,font("arial",20,"bold"),text=nowTime,bd=10 ,bg="black", #fg="white", anchor="w").pack()


#====================================debugged========================


shirt = IntVar()
pant = IntVar()
sale = IntVar()
buy = IntVar()
deposite = IntVar()
withdraw = IntVar()
coat = IntVar()
order = IntVar()
total = IntVar()
out = IntVar()
before = IntVar() #order before the 60
stock = IntVar()
delivery = IntVar()


#########################main_gate######################




def _calculation():

    shirt_mm = shirt.get()
    pant_mm = pant.get()
    sale_mm = sale.get()
    buy_mm = buy.get()
    deposite_mm = deposite.get()
    withdraw_mm = withdraw.get()
    coat_mm = coat.get()
    order_mm = order.get()
    total_mm = total.get()

    time = datetime.now()
    day = time.day
    month = time.month
    hour = time.hour
    second = time.second
    year = time.year
    minute = time.minute

    #setting the filename using the loop

    #file = open("1{}".format())

    '''for i in range(5):
        if os.path.isfile(i):
            pass
        else:
            file = open("{}.txt".format(i+1), "w+")
             created with name {}".format(file))'''

    #creating the filenames with append =1 if the name already existed
    file_name = "r.txt"
    if os.path.isfile(file_name):
        expand = 1
        while True:
            expand += 1
            new_file_name = file_name.split(".txt")[0] + str(expand) + ".txt"
            if os.path.isfile(new_file_name): #if the newfilename exists 
                print("using the file {}".format(new_file_name))
                #file = open("{}".format(new_file_name), "w+")
                continue
            else:
                file_name = open(new_file_name, "w+")
                print("creating the file {}".format(file_name))
                #file = open("{}".format(file_name), "w+")
                break

                file_name = "fil.txt"


    file = open("{}".format(file_name),"w+")
            

    totalx = shirt_mm+pant_mm+sale_mm+buy_mm+deposite_mm+withdraw_mm+coat_mm+order_mm

    file.write("Total:-{}".format(totalx))
    file.write("shirt:-{}".format(shirt_mm))
    file.write("pant_mm:-{}".format(pant_mm))
    file.write("sale_mm:-{}".format(sale_mm))
    file.write("buy_mm:-{}".format(buy_mm))
    file.write("deposite_mm:-{}".format(deposite_mm))
    file.write("withdraw_mm:-{}".format(withdraw_mm))
    file.write("coat:-{}".format(coat_mm))
    file.write("order:-{}".format(order_mm))
    reading = file.readlines()
    file.close()
#after wards set the total from here total.set

#++++++++++++++++++++++++++++++Varibales_inset+++++++++++++++++++++++++++++++++

order_bef = IntVar()
stock_full = IntVar()
shrting = IntVar()
pant = IntVar()
sari = IntVar()
order_info = IntVar()
delivery_report = IntVar()
daily_info = IntVar()
sales = IntVar()
buy = IntVar()
total_bank = IntVar()
bank_deposite = IntVar()
bank_withdraw = IntVar()
due_amount = IntVar()
order_info = IntVar()
daily_cash = IntVar()
cus_name = IntVar()
cus_no = IntVar()
employee = IntVar()

###############################class of algoriths#########################


class __main():


    def __init__(self):
        self.order = order

    def __order_info(self):

        self.now = datetime()
        self.hour = now.hour
        self.minute = now.minute
        self.second = now.second
        self.year = now.year
        self.month = now.month
        self.day = now.day

        self.record_time = record_time


        if self.hour == self.record_timeD:
            print("the time for the product is actually %s left" %(self.hour-self.record_timeD))

#++++++++++++++++++++++++++++++++++++++++tinydb example++++++++++++++++++++++
#db = TinyDB("/databse/d4ta.json")
#db.insert({"cus_number":"98938232", "cus_name":"rupen"})

#def no_y():
 #   lis = db.all()
################Info===============
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

#==============================another windows about me=====================

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

    ima = StringVar()
    imageloc=Entry(win1,font=("arial",16,"italic"),bg="black",fg="white",bd=5,insertwidth=1,relief=GROOVE,textvariable=ima).pack()
    imageButt=Button(win1,font=("arial",20, "bold"),bd=5,bg="white",fg="white",command= lambda: _image(image)).pack()

    '''def _image(image):


        image = image.set(imageloc)
        return image
    #image = Image.open("/root/Desktop/Desktop/anonymous/5.png")

    imae = Label(win1,font=("arial", 20,"italic"),width=300, height=168,bg="black",fg="white", text=image,relief=FLAT).pack()

    win1.mainloop()'''


#=============================getting all the infos ========================

def _price_inputs():
    win2 = Toplevel()
    win2.title("This is going to the section for the price inputs")
    win2.geometry("1600x800")

    framex = Frame(win2,width=1600,bg="RoyalBlue4",height=100,relief=GROOVE).pack(side=TOP)
    frame1 = Frame(win2,width=775, height=750,bg="white", relief=SUNKEN).pack()
    frame2 = Frame(win2, width=775,height=750,bg="black", relief=FLAT).pack()

    #==++++===========================title=============================

    llb1 = Label(framex,font=("arial", 20,"italic"),bg="powder blue",fg="green",text="INPUT THE PRICES",relief=GROOVE).pack()

    


    win2.mainloop()

###########################sending emails############################


def __send_email():

    '''import smtplib

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.starttls()

    _file = open("/root/Desktop/Desktop/python/")

    gmail.login("username", "password")

    msg = "YOUR MESSAGE"

    gmail.sendmail("your email adress", "the")
    gmail.quit()'''

    dialog = Tk()
    dialog.title("Send emails")
    dialog.geometry("800x800")

    dframe = Frame(dialog,width=800,height=800,bg="white",relief=SUNKEN).pack()
    email = StringVar()
    password = StringVar()

    semail = StringVar()
    spassword = StringVar()

    label = Label(dframe, font=("arial",16, "bold"), fg="white", bg="black", text="your_email").pack(side=LEFT)
    entry1 = Entry(dframe, font=("arial",16,"bold"), fg="white",bg="black", textvariable=email,insertwidth=1,bd=5).pack(side=RIGHT)

    label1 = Label(dframe, font=("arial",16, "bold"), fg="white", bg="black", text="password", relief=SUNKEN).pack()
    entry2 = Entry(dframe,font=("arial", 16 ,"bold"),textvariable=password, insertwidth=1,bd=5).pack(side=RIGHT)

    Label2 =Label(dframe,font=("arial",16, "bold"),fg="white",bg="black", text="sender_email",relief=SUNKEN).pack(side=LEFT)
    entry2 = Entry(dframe,font=("arial",16, "bold"),bd=5,fg="white",bg="black",textvariable=semail,insertwidth=1).pack(side=LEFT)

    label3 = Label(dframe,font=("arial",16,"bold"),fg="white",bg="black",text="sender_password", relief=SUNKEN).pack(side=LEFT)
    entry3= Entry(dframe,font=("arial",16,"bold"),fg="white",textvariable=spassword,insertwidth=1,relief=SUNKEN).pack()



    dialog.mainloop()



#btnEmail = Button(root,font=("arial", 16, "bold"), bg="black",fg="white",text="email",command=lambda: __send_email(),relief=GROOVE).pack()
#================================next section===========================




fix = Button(root, bd=10,bg="black",fg="white",command=_price_inputs,relief=GROOVE).pack(side=BOTTOM)
btnru = Button(root, font=("arial 20 bold"),bd=20, bg="black",fg="white",text="click",command=ano_win1,relief=GROOVE).pack(side=BOTTOM)



#fucking mazing yr coding
def column(col):
    for coll in col:
        call=cal+1

    return call

#def yes_y():
 #   rupe = Toplevel(root)
  #  rupe.title("this is second window")
   # return

#def no_y():
    #nos = Toplevel(root)
    #nos.title("this is nos window")
    #return


a = Entry(f2,font=("arial", 20,"bold"), textvariable=text_Input, bd=30, insertwidth=4,
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
b=Entry(f1,font=("arial", 16, "bold"), textvariable=rand, bd=10,insertwidth=4,fg="white",bg="black", justify = "left")
b.grid(row=0,column=1)
#img = "/root/Desktop/Desktop/python/projects/prj1_Botik/1.jpg"
#root.ima = Image.open(img)
#Label (root,bg="white",width=120,height=120, image=ima).pack()

bill_in = StringVar()
bill_out = StringVar()

shrting=Label(f1,font=("arial", 20, "bold"), text="Shirting:",bg="powder blue", fg="black",anchor="w",relief=GROOVE).grid(row=1,column=0)
shirts=Entry(f1,font=("arial", 16, "italic"), bd=10, textvariable=shirt, insertwidth=1,bg="black",fg="white", justify="left").grid(row=2,column=0)


owner=Button(root,padx=16,pady=16, font=("arial",12, "bold"),text="info", bd=8,bg="black",command=ano_win1,fg="white",relief=RAISED).pack(side=LEFT)
yes=Button(root,padx=16,pady=16,font=("arial",12, "bold"),text="Done",bd=8,bg="black", fg="white", command=_calculation(),relief=RAISED).pack(side=RIGHT)

panting=Label(f1,font=("arial",20, "bold"), text="pant_mm:", bg="powder blue",fg="black",anchor="w",relief=GROOVE).grid(row=1,column=1)
pantx=Entry(f1,font=("arial",16, "bold"), textvariable=pant, insertwidth=1, bd=10,bg="black",fg="white", justify="left").grid(row=2,column=1)


sales=Label(f1,font=("arial",16, "bold"), text="sales_total:",bg="powder blue",fg="black",anchor="w",bd=8,relief=GROOVE).grid(row=1,column=2)
salex=Entry(f1,font=("arial",16, "bold"),bg="black",fg="white",textvariable=sale,insertwidth=1,bd=10,justify="left").grid(row=2,column=2)

buying=Label(f1,font=("arial",16, "bold"), text="buying_something:  ",bg="powder blue",fg="black", anchor="e", relief=GROOVE).grid(row=3,column=0)
buyx=Entry(f1,font=("arial", 16, "bold"), textvariable=buy, insertwidth=1, bd=10,bg="black", fg="white", justify="left").grid(row=4,column=0)

Bank_Total=Label(f1,font=("arial",16,"bold"),text="Bank_Deposite: ", bg="powder blue", fg="black", anchor="e",relief=GROOVE).grid(row=3, column=1)
depositex=Entry(f1,font=("arial",16,"bold"),bd=10, textvariable=deposite, bg="black", fg="white", justify="left").grid(row=4, column=1)

lblBankwith=Label(f1, font=("arial", 16, "bold"),fg="black",bg="powder blue",text="Bank_Withdraw", anchor="e",relief=GROOVE).grid(row=3,column=2)
withdrawx=Entry(f1,font=("arial",16, "bold"),bd=10, fg="white",bg="black", textvariable=withdraw, insertwidth=1).grid(row=4,column=2)


coating=Label(f1, font=("arial", 16, "bold"),text="coat_mm:", bg="powder blue",fg="black",anchor="e").grid(row=5,column=0)
coatx=Entry(f1, font=("arial", 16, "bold"), bg="black", fg="white",
          textvariable=coat, insertwidth=1, justify="left",bd=10).grid(row=6,column=0)

lablsari=Label(f1,font=("arial", 16, "bold"), bg="powder blue",text="sari mm:", fg="black",anchor="e",relief=GROOVE).grid(row=5,column=1)
sarix=Entry(f1, font=("arial", 16, "bold"), bg="black",bd=10, fg="white",textvariable=sari, insertwidth=1).grid(row=6,column=1)

buying=Label(f1,font=("arial", 16, "bold"), bg="powder blue",text="buy_info:",fg="black",anchor="e",relief=GROOVE).grid(row=7,column=0)
buyx=Entry(f1,font=("arial",16, "bold"),bd=8, fg="white",bg="black",textvariable=buy,insertwidth=1).grid(row=8,column=0)

outgoing =Label(f1, font=("arial", 16, "bold"), bg="powder blue", text="outgoing:", fg="black",anchor="e",relief=GROOVE).grid(row=7,column=1)
outx=Entry(f1,font=("arial", 16, "bold"),textvariable=out, bd=8,fg="white",bg="black",insertwidth=1).grid(row=8,column=1)

ordering=Label(f1,font=("arial",16,"bold"),bg="powder blue",text="order_info:",fg="black",anchor="e",relief=GROOVE).grid(row=9,column=0)
orderx=Entry(f1,font=("arial",16,"bold"),insertwidth=1, textvariable=order,bd=8,fg="white",bg="black").grid(row=10,column=0)

lblcustomer=Label(f1,font=("arial",16,"bold"),bg="powder blue",text="cus_name:",fg="black",anchor="e",relief=GROOVE).grid(row=9,column=1)
no=Entry(f1,font=("arial",16, "bold"),bd=8,bg="black",fg="white",insertwidth=1, textvariable=cus_name).grid(row=10,column=1)

lblmonthly=Label(f1, font=("arial",16,"bold"),bg="powder blue",text="monthly:",fg="black",anchor="e",relief=GROOVE).grid(row=5,column=2)
monthly=StringVar()
monthx=Entry(f1,font=("arial",16,"bold"),show="blank",bg="black",textvariable=monthly,insertwidth=1,fg="white",bd=10).grid(row=6,column=2)

lbltotal=Label(f1, font=("arial", 16, "bold"),bg="powder blue",text="Total:",fg="black").grid(row=7,column=2)
totalx=Entry(f1, font=("arial", 16, "bold"),bg="black",textvariable=total,fg="white",insertwidth=1,bd=10).grid(row=8,column=2)

lblemployee = Label(f1,font=("arial", 16, "bold"),bg="powder blue",text="employee name:",fg="black",anchor="e",relief=GROOVE).grid(row=9,column=2)
employx= Entry(f1,font=("arial", 16,"bold"),textvariable=employee,insertwidth=1,bg="black",fg="white",bd=10).grid(row=10,column=2)


###############################database for the project######################


'''def __database():


    db = TinyDB("/records.json")

    #print(monthly)
    #print(b)
    #fuck = c.get()

    a = order_bef.get()
    b = stock_full.get()
    c = shrting.get()
    d = pant.get()
    e = sari.get()
    f = order_info.get()
    g = delivery_report.get()
    h = daily_info.get()
    i = sales.get()
    j = buy.get()
    k = total_bank.get()
    l = bank_deposite.get()
    m = bank_withdraw.get()
    n = due_amount.get()
    o = order_info.get()
    p = daily_cash.get()
    q = cus_name.get()
    r = cus_no.get()
    s = employee.get()

    files = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": "", "h": "", "i": "", "j": ""
        , "k": "", "l": "", "m": "", "n": "", "o": "", "p": "", "q": "", "r": "", "s": ""}

    db.insert({"total": a }),
    db.insert({"regrds":"reference"}),
    db.insert({"day_income":"billion"}),
    db.insert({"day_outgoing":"billout"}),
    db.insert({"bankdeposit":"bankdepo"}),
    db.insert({"full_stock":"stock"}),
    db.insert({"shirt_mm":"shirt"}),
    db.insert({"bankwithdraw":"bankwith"}),
    db.insert({"pantmm":"pant"}),
    db.insert({"sarimm":"sari"}),
    db.insert({"orderday":"orderinfo"}),
    db.insert({"salling":"sales"}),
    db.insert({"buying":"buy"}),
    db.insert({"customern":"customer"}),
    db.insert({"monthly_info":"monthly"}),
    db.insert({"totaldy":"total"}),
    db.insert({"employeid":"employee"})

    for db in range(1):
        print(db)

    files = list(files)
    file = open("/file.txt", "wb")
    da = ""
    for data in files:
        if len(data) != 0:
            print("this is are the files written in python\\n check the file.txt for debug ")
            da += data
            print(data)
    da = int(da)
    file.write(da)

    try:
        file = open("/records.txt", "r")
    except:
        print("creating the file from script {}".format(__file__))
        file = open("/records.txt","w")
    finally:
        pass

        
        check = os.path.isfile("/records.txt")
        if check:
            for item in db:
                data = open("/records.txt","wb")
                #with open("/records.txt","wb") as file:
                #pickle.dump(item, data)
                #file.close()
                #file1 = pickle.load(file)
                if len(item) == len(file1):
                    break

                if item != file:
                    #item = str(item)
                    file.write("%s" %(item))
                    time.sleep(1)
                    print("done writing to the file")

                    
    #for item in db:
    with open("/records.txt", "rb") as file:
        
        reading = file1
        if len(reading) != None:
            print("its printed")
        print(reading)
    file.close()
    

    #db.insert({"name":"Rupen Gurung"})

    name = Query()

    #db(name.type == "changed")

    d = datetime.now()

    month = str(d.month)
    day = str(d.day)
    year = str(d.year)
    hour = str(d.hour)
    minute = str(d.minute)
    second = str(d.second)
    between = str(":")'''

'''def __time(infos):

        time = datetime.now()
        day = str(time.day)
        month = str(time.month)
        hour = str(time.hour)
        second = str(time.second)
        year = str(time.year)
        minute = str(time.minute)

        #assuming the infos as the order taken that will be notified before the
        #60 hours


        #changing all the formats to the seconds that will be easy for the #calculation


        #first calculating seconds in one day that will ease all the further operations

        daysec = (24*60) * 60 * 60
        ###
        ##this is will be easy now 

        yearSec = daysec * 365
        month = daysec * 30
        daySec = daysec
        hourSec =  60 * 60 * 60
        minuteSec = 60 * 60



files = {"a":"", "b":"","c":"","d":"","e":"","f":"","g":"","h":"","i":"","j":""
        ,"k":"","l":"","m":"","n":"","o":"","p":"","q":"","r":"","s":""}'''


#files = list(files)
'''for data in files:
    if len(data) != 0:
        print(data)'''


#lenght = len(db)
##this will show the recorded bill numbers

def bill_in():
    ##assuming the variable as bill number .get var

    bill = bill_in.get()
    billo = bill_out.get()

    bills = tinydb.TinyDb("/bills.json")

    while bill or billo != None:
        bills.insert({"billInput": bill, "billOutput": billo})

    win = Toplevel()
    win.title("bills")

    winF = Frame(win, bg="black",relief=SUNKEN).pack()
    winE = Entry(winF, insertwidth=10,insertheight=10,fg="white",bg="black",textvariable=bills).pack()
    win.mainloop()
#l
#            command=bill_in).pack(anchor=NE)


root.mainloop()
#__database()


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

