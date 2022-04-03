from mysql import *
import mysql.connector as mysql

def connect():
	connexion = mysql.connect (
		user='root',
		password='root',
		database='projet_reseau')
	return connexion

def validerCredential(data: tuple) -> bool:
	try:
		db = connect()
		cursor = db.cursor()
		query = "SELECT * from user WHERE email=%s AND password=%s"
		cursor.execute(query,data)
		record = cursor.fetchone()
		print(record)
		db.close()
		if record is not None:
			return True
		else:
			return False
			
	except mysql.Error as error:
		print ("Erreur : {}".format(error))
		db.close()
		return False


def createUser(data: tuple) -> bool:
	try:
		db = connect()
		cursor = db.cursor()
		cursor.execute("INSERT INTO user(nom,prenom,email,password) VALUES (%s,%s,%s,%s)",data)
		db.commit()
		db.close()
		return True 
	except mysql.Error as error:
		db.rollback()
		print ("Erreur : {}".format(error))
		db.close()
		return False
		
#if __name__ == '__main__':
#	data = ('ccb@projet-reseau.sn','root')
#	print(validerCredential(data))
