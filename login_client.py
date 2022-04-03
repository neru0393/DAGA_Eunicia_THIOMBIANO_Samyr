#!/usr/bin/ python3

import socket
import json
from tkinter import *
from tkinter import messagebox
import subprocess

def connectToServer():
	host = 'localhost'
	port = 55000
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((host, port))
	return client

def receive(client):
	res = client.recv(512).decode("utf-8")
	return res
root=Tk()
root.title("Connexion")
root.geometry("1000x500")
root.resizable(False,False)


def connexion():

	email = emailValue.get()
	password = passwordValue.get()
	passwordConfirm = passwordConfirmValue.get()
	if (emailEntry.index("end") == 0 or
		passwordEntry.index("end") == 0 or
		passwordConfirmEntry.index("end") == 0 ) :
		messagebox.showwarning('Avertissement', 
		'Veuillez remplir tous les champs')
	elif (password != passwordConfirm) :
		messagebox.showwarning('Avertissement', 
		'Veuillez rentrer des mots de passe identiques')
	else :
		print("Connexion en cours ")
		data = (email,password)
		donnees = {"method":'GET',"data":data}
		requete = json.dumps(donnees)
		client = connectToServer()
		client.sendall(requete.encode("utf-8"))
		res = receive(client)
		if res == "True":
		
			messagebox.showinfo("Statut", 
			"Connexion Ok")
			print("Email : " + email)
			emailEntry.delete(0, END)
			passwordEntry.delete(0, END)
			passwordConfirmEntry.delete(0, END)
			emailEntry.focus_set()

			subprocess.run(["firefox", "projet-reseau.sn"])
		else:
			messagebox.showerror('Erreur', 
		'Identifiants inccorects')
			
Label(root, text="Page de connexion",font="arial 16").pack(pady=50)#.grid(row=0, column=1)#

Label(text="Email", font=12).place(x=50,y=150)#.grid(row=1, column=0)
Label(text="Password", font=12).place(x=50,y=200)#.grid(row=2, column=0)
Label(text="Password Confirm", font=12).place(x=50,y=250)#.grid(row=3, column=0)#.

#Entry
emailValue=StringVar()
passwordValue=StringVar()
passwordConfirmValue=StringVar()

emailEntry=Entry(root,textvariable=emailValue,width=25,bd=2,font=12)
passwordEntry=Entry(root,show='*',textvariable=passwordValue,width=25,bd=2,font=12)
passwordConfirmEntry=Entry(root,show='*',textvariable=passwordConfirmValue,width=25,bd=2,font=12)


emailEntry.place(x=400,y=150)#.grid(row=1, column=1)#
passwordEntry.place(x=400,y=200)#.grid(row=2, column=1)#
passwordConfirmEntry.place(x=400,y=250)#.grid(row=3, column=1)#


#Submit button
Button(text="Se connecter",font=12,width=10,height=2,command=connexion).place(x=350,y=350)#.grid(row=5, column=1)#



#root.mainloop()


if __name__ == '__main__':
	#connectToServer()
	root.mainloop()
