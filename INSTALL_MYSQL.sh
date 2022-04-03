#!/bin/bash

#INSTALLATION DE MYSQL
echo "*****Installation de MySQL*****";

#Mise a jour
sudo apt-get update -y;
sudo apt-get upgrade -y;

#Installation du serveur
#sudo apt-get install mysql-server -y;

#Installation du client
#sudo apt-get install mysql-client -y;

#Affichage de la version
#mysql --version;

#Redemarrage du service
#sudo systemctl restart mysql;

#Affichage du statut du service
#sudo systemctl status mysql

#Création de la base de données 
mysql -e 'CREATE DATABASE projet_reseau';

#Création de la table
Mysql -e 'USE projet_reseau;CREATE TABLE user(identifiant int(5),nom varchar(20),prenom varchar(20), password(20), PRIMARY KEY(identifiant))';