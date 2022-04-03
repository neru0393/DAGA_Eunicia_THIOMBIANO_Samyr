# PROJET DE PROGRAMMATION RESEAU  
## DAGA Eunicia Neruda
## THIOMBIANO Samyr Christian Yentéma

## Environnement d'exécution
  * VirtualBox
  * Ubuntu Desktop X 3
  * Python 3.8
  
***

## PARTIE 0
  * Adresse fixe du serveur.  
    Nous avons utilisés ```netplan``` pour fixer notre adresse.  
    
    ![netplan](https://user-images.githubusercontent.com/96637804/161450008-6648ccc8-6ebd-42c1-ab00-694122cd90c5.png)

  * Configuration du DNS.  
     Nous avons utilises le paquet 
     ``` bind9 ``` pour configurer notre DNS.  
     
     Installation de ```bind9``` : 
     ```
    sudo apt update
    sudo apt install bind9 bind9utils bind9-dnsutils bind9-doc bind9-host
     ```
    Nous avons principalement configurés 3 fichers concernant bind9 : 
    
    ![local](https://user-images.githubusercontent.com/96637804/161449805-3a1e5ac7-e3fd-4eaf-b5b2-325542512087.png)
    
    ![zone](https://user-images.githubusercontent.com/96637804/161449825-32ebb411-e2d7-40e1-81e5-90f263ecd9be.png)
 
    ![reverse](https://user-images.githubusercontent.com/96637804/161449832-519b3a98-577d-40c7-b7de-acb607057857.png)
  
  * Configuration du DHCP.  
    Nous avons utilisés ```isc-dhcp-server``` pour mettre en place le service DHCP.  
    
    Installation de ```isc-dhcp-server``` :  
    ```
    sudo apt-get update
    sudo apt-get install isc-dhcp-server -y
    ```
    
    Configuration principale du service DHCP :  
    ![dhcp](https://user-images.githubusercontent.com/96637804/161450254-d947a0f7-f3f4-4232-9efc-2e01d8e7e849.png)

***

## PARTIE 1
  * Installation de ```MySQL``` :  
    Pour installer ```MySQL``` il suffit de lancer le script ```INSTALL_MYSQL.sh``` en tapant ./INSTALL_MYSQL.sh
    
  * Installation de ```iRedMail``` :  
    Pour installer ```iRedMail``` il suffit de lancer le script ```INSTALL_IREDMAIL_DEPENDENCIES.sh``` en tapant ./INSTALL_IREDMAIL_DEPENDENCIES.sh.  
    Nous renseignerons ensuite des informations à la demande comme le nom de notre domaine, le mot de passe de l'utilisateur root MySQL, le mot de passe pour le compte root iRedMail.  
    Nous laissons toutes les autres configurations par défaut.   

  * Installation de ```Wireshark``` :  
    ```
    sudo add-apt-repository universe
    sudo apt install wireshark
    ```
    Nous laissons les paramètres par défaut pour l'installation.  
    
  * Politique ```UFW``` :  
    Nous avons mis en place une politque de sécurité permettant de bloquer toutes les connections entrantes sauf celles provenants de la ```plage d'adresse fixée``` et sur le port ```55000```. 
    ```
    sudo ufw default deny incoming
    sudo ufw allow from 192.168.10.0/24 to any port 55000
    sudo ufw enable

    ```
***

## PARTIE 2
  * Scripts côté ```client``` : 
    Les scripts côté ```client``` sont ```login_client.py``` et ```registration_client.py```.  
    Le script ```login_client.py``` permet d'afficher l'interface de connexion et d'ouvrir une page du navigateur ```Firefox``` lorsque les identifiants renseignés par le client sont validés par le serveur (client authentifié).  
    Une page d'erreur est affichée en cas d'erreur.  
    Le script ```registration_client.py``` permet d'afficher l'interface d'enregistrement d'utilisateurs.  
    Une page d'erreur est affichée en cas d'erreur.  
    
  * Scripts côté ```serveur``` :  
    Les scripts coté  ```serveur``` permettent la vérification des informations si l'utilisateur a soumis une requête de type ```GET``` et l'enregistrement pour une requête de type ```POST```.  
    
  * Script d'analyse :   
    Ce script permet l'analyse des packets échangés lors d'une connexion ou d'un enregistrement.    
    
  * Script de mailing :  
    Ce script permet d'envoyer un rapport d'analyse a notre mail ```postmaster@projet-reseau.sn```
     

