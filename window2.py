#!/usr/bin/env python
import os, sys
from tkinter import *

root = Tk()
def window_2():
	root.title("this will be the price update section")
	root.geometry("1600x800+0+0")

	window2 = Frame(root,bg="powder blue",width=1600, height=500).pack(side=BOTTOM)
	window02 = Frame(root, bg="green",width=1600,height=300).pack(side=TOP)

	lbl1 = Label(window2, padx=16,pady=20,font=("arial 20 bold"),text="fucking",bg="blue",fg="black", relief=GROOVE).pack()

	btn1 = Button(window02, font=("arial 20 bold"), pady=20,padx=20, text="hello",
				bd=10,bg="black",fg="white",command=hello).pack(side=RIGHT)

	def hello():
		hellow = "hellow world"
		return hellow





if __name__ == "__main__":
	window_2()