#!/usr/bin/env python
#####author::Rupen_Gurung::########

#algoriiths for the botique project

from tkinter import *


root = Tk()

class algo_botique:
	def incoming_cash(self, today_tran,today_inco):
		
		self.today_inco = today_inco
		self.today_tran = today_tran
		self.order_info = order_info
		self.today_saling = today_sales
		self.daily_income = daily_income
		self.today_total = today_total

		self.order_info = order_info.get()
		self.bank_withdraw = bank_withdraw
		self.buy = buy

stock_full = StringVar() #this we will count as full stock
shrting = StringVar()#this does not
pant = StringVar()#this does not
sari = StringVar()#this  sdjfkad
order_info = StringVar()#outgoing
delivery_report = StringVar()#this does not
daily_info = StringVar()#daily calculation
sales = StringVar()#incoming
buy = StringVar()#outgoing
total_bank = StringVar()#total
bank_deposite = StringVar()#nothing
bank_withdraw = StringVar()#outgoing
due_amount = StringVar()#outgoing
order_info = StringVar()#nothing
daily_cash = StringVar()#daily_total
cus_name = StringVar()#info
cus_no = StringVar()#info



incoming=("sales","order_info")
outgoing=("buy", "bank_withdraw", "due_amount")


global s
global o
global b
global w
global d


#__________________________________Incoming_Variable__________________________

s = sales 

#__________________________________Outgoing_Variable___________________________

o = order_info
w = bank_withdraw
b = buy
d = due_amount


#incomplete function

def todays_info(total):
		total = int((s+o)-(b+w+d))
		if total != 0:
			print("yeah the totals out")
			messagebox.showinfo("total of the day", "your total of today is: %s" %(total))
		else:
			messagebox.showinfo("total ", "what the fuck the is no calculation today")


def _operations(self,total, f, s, t=None,ff=None,fi=None,
								si=None,se=None,ei=None):
		
		self.total = self.total
		self.f = f
		self.s = s
		self.t = t
		self.f = f
		self.fi = fi
		self.si = si
		self.se = se
		self.ei = ei

		global operator

		operator = self.operator
		self.operator = operator


		while self.f or self.s or self.t or self.f or self.fi or self.si or self.se or self.ei != None:

			return total  

s = algo_botique()
root.mainloop()






























