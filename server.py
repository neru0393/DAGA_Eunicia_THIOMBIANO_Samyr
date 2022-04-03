import socket
import json
import time
import database

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55000
ADDRESS = ('localhost',PORT)

def openServer(buffer=1024):
	serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serveur.bind(ADDRESS)
	serveur.listen(5)
	print ("Serveur : ",ADDRESS[0])
	print ("Port : ",ADDRESS[1])
	requete = ""
	while True:
		client, infosClient = serveur.accept()
		print("Client connecte. Adresse " +infosClient[0])
		
		requete = client.recv(buffer).decode("utf-8")
		
		donnees = json.loads(requete)
		print(donnees)
		
		if donnees.get("method") == "POST":
			print("Demande d'Insertion")
			data = donnees.get("data")
			database.createUser(data)
			client.send("OK".encode("utf-8"))
		elif donnees.get("method") == "GET":
			print("Demande de Connexion")
			data = donnees.get("data")
			client.send(str(database.validerCredential(data)).encode("utf-8"))
			

if __name__ == '__main__':
	openServer()

