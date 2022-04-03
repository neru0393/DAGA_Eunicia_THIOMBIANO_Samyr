#!/bin/bash

#INSTALLATION DE IREDMAIL
echo "*****Installation de IREDMAIL*****";

#Installation de wget
sudo apt-get install wget -y;

#Telechargement du package
wget "https://github.com/iredmail/iRedMail/archive/1.5.2.tar.gz";

#Extraction du package
tar xvf 1.5.2.tar.gz;

#Execution
cd iRedMail-1.5.2/ ;
chmod a+x iRedMail.sh;
sudo bash iRedMail.sh;

#Redemarrage de la machine
