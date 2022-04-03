#!/usr/bin/ python3
import json
import socket
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Inscription")
root.geometry("1000x600")
root.resizable(False,False)

def connectToServer():
	host = 'localhost'
	port = 55000
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((host, port))
	return client

def receiveFromServer(client):
	res = client.recv(512).decode("utf-8")
	return res
	
def inscription():

	nom = nomValue.get()
	prenom = prenomValue.get()
	email = emailValue.get()
	password = passwordValue.get()
	passwordConfirm = passwordConfirmValue.get()
	
	if (nomEntry.index("end") == 0 or
		prenomEntry.index("end") == 0 or
		emailEntry.index("end") == 0 or
		passwordEntry.index("end") == 0 or
		passwordConfirmEntry.index("end") == 0) :
		messagebox.showwarning('Avertissement', 
		'Veuillez remplir tous les champs')
	elif (password != passwordConfirm) :
		messagebox.showwarning('Avertissement', 
		'Veuillez rentrer des mots de passe identiques')
	else :
		print("Inscription en cours ")
		
		
		data = (nom,prenom,email,password)
		donnees = {"method":'POST',"data":data}
		requete = json.dumps(donnees)
		client = connectToServer()
		client.sendall(requete.encode("utf-8"))
		res = receiveFromServer(client)
		print(res)
		messagebox.showinfo("Statut", 
					"Formulaire envoye")
		print("Nom : " + nom)
		print("Prenom : " + prenom)
		nomEntry.delete(0, END)
		prenomEntry.delete(0, END)
		emailEntry.delete(0, END)
		passwordEntry.delete(0, END)
		passwordConfirmEntry.delete(0, END)
		nomEntry.focus_set()
		
		
			
			
Label(root, text="Formulaire d'inscription",font="arial 16").pack(pady=50)

Label(text="Nom", font=12).place(x=50,y=150)
Label(text="Prenom", font=12).place(x=50,y=200)
Label(text="Email", font=12).place(x=50,y=250)
Label(text="Password", font=12).place(x=50,y=300)
Label(text="Password Confirm", font=12).place(x=50,y=350)

#Entry
nomValue=StringVar()
prenomValue=StringVar()
emailValue=StringVar()
passwordValue=StringVar()
passwordConfirmValue=StringVar()

nomEntry=Entry(root,textvariable=nomValue,width=25,bd=2,font=12)
prenomEntry=Entry(root,textvariable=prenomValue,width=25,bd=2,font=12)
emailEntry=Entry(root,textvariable=emailValue,width=25,bd=2,font=12)
passwordEntry=Entry(root,show='*',textvariable=passwordValue,width=25,bd=2,font=12)
passwordConfirmEntry=Entry(root,show='*',textvariable=passwordConfirmValue,width=25,bd=2,font=12)


nomEntry.place(x=400,y=150)
prenomEntry.place(x=400,y=200)
emailEntry.place(x=400,y=250)
passwordEntry.place(x=400,y=300)
passwordConfirmEntry.place(x=400,y=350)


#Submit button
Button(text="S'inscrire",font=12,width=10,height=2,command=inscription).place(x=350,y=450)




root.mainloop()


#if __name__ == '__main__':
