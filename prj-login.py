
def check_info():

	file=open("/fuck.db", "wb")

	global username
	global password

	username = entuser.get()
	password = entpass.get()

	dic = {"user":"fuck","user2":"fuck2"}  

	passe = dic.values()
	usern = dic.keys()

	#for user in username:
	#	for passwords in password:
	#	passs += passwords
	#	usern += user

	if username not in usern:
		if password not in passe:
			messagebox.showinfo("!!!alert","Password or Username not match!!!!!") 

	else: 
		messagebox.shobwinfo("welcome","welcome %s" %(username))


def register_ing():
	global username 
	global password

	if username not in dic:
		file.dict[new]=username
		file.dict[password]=passw

	else:
		um = Toplevel(main)
		um.title("!!!alert")
		alert =Label(um,text="username already taken",bg="white",fg="red").pack()
		



main.mainloop()
#img=Image			

#def main_win():
#	file = open("/fuck.db", "wb")
#	file.readlines()
#	password = file.password([:])


#	if "sunil" or "suman" in user:
#		if "suman" in 
