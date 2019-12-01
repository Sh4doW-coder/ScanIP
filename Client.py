# -*- coding: utf-8 -*-

import socket # Nécessaire pour ouvrir une connexion
import PoolAdresse #On fait appel aux fonctions présentes dans PoolAdresse.py
import csv	#Nécessaire pour manipuler facilement les fichiers CSV
import smtplib
import datetime
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def Connexion(ip, port, timeout,message): #Permet d'ouvrir une connexion
	try:
		connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connexion_avec_serveur.settimeout(timeout)	#On définit le temps au bout du quel la connexion est abandonnée si le serveur ne répond pas
		connexion_avec_serveur.connect((ip, port))
		msg_a_envoyer =message.encode()
		
		connexion_avec_serveur.send(msg_a_envoyer)
		msg_recu = connexion_avec_serveur.recv(1024)
		msg_recu = msg_recu.decode()
		
		print("\n***************************************************")
		print(msg_recu)
		print("***************************************************\n")
		
		connexion_avec_serveur.close()
		resultatConnexion = msg_recu
	except:
		print("Impossible de joindre le serveur "+ip)
		resultatConnexion = "Connexion impossible pour le serveur "+ ip + ':' + str(port)

	return resultatConnexion


def ScanAuto(port, timeout): #Permet de scanner automatiquement l'ensemble des adresses du réseau local
	hote=PoolAdresse.PoolAPing()
	taille=len(hote)
	for i in range(0,taille):
		ip=hote[i]
		Ecrire_Historique("Scan automatique : "+Connexion(ip,port,timeout,"GiveAllInfo"))

def ScanIp(port,timeout,ip): #Permet d'ouvrir une connexion et d'enregistrer le résultat dans les logs
	Ecrire_Historique("Scan d'@IP : "+ Connexion(ip,port,timeout,"GiveAllInfo") )

def ScanCSV(fichier, port, timeout): #Permet d'ouvrir une connexion vers toutes les adresses présentes dans le fichier CSV fourni

	adresses = Lire_CSV(fichier)	
	for adresse in adresses:
		Ecrire_Historique("Scan CSV : "+Connexion(adresse,port,timeout,"GiveAllInfo"))

def Lire_CSV(fichier): #On fournit un fichier CSV contenant des adresses IP
	adresse_valables = []
	f=open(fichier,'r') #On ouvre le fichier fournit en mode lecture (read)
	
	contenu = csv.reader(f,delimiter=';')
	for ligne in contenu:	#Pour chaque ligne :
		for champ in ligne:		#Pour chaque champ :
			if est_IP(champ): #On vérifie si le champ est une adresse IP
				adresse_valables.append(champ)
			
	f.close()
	return adresse_valables	#retourne un tableau contenant dans chaque case une adresse ip

def est_IP(adresse):	# retourne True si la chaine fournie est une adresse IP
	if len(adresse.split('.')) != 4 : return False #Si l'adresse fournit n'as pas 4 champs séparés par des points
	for nombre in adresse.split('.'):
		if int(nombre) > 255 or int(nombre) < 0 : return False #Si l'un des 4 nombres de l'adresse IP n'est pas compris entre 0 et 255
	return True

def Ecrire_Historique(resultat): #Ecrit le fichier log
	heure = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S') 
	mon_fichier = open("connexions.log", "a")
	mon_fichier.write(heure + ' ' + resultat + '\n')
	mon_fichier.close()


def EnvoieEmail(Email):
	#Element de base du mail
	email = 'scanipofficiel@gmail.com'
	password = 'Scaniprt'
	send_to_email = Email
	subject = 'Resulat du scan - ScanIP'
	message = '''Bonjour,
	Vous trouverez ci-joint les résultats du scan que vous avez réalisez.
Cordialement, Le logiciel lui-meme.'''

	file_location = './connexions.log'

	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = send_to_email
	msg['Subject'] = subject

	msg.attach(MIMEText(message, 'plain'))

	# Initialisation de la piece joint 
	filename = os.path.basename(file_location)
	attachment = open(file_location, "rb")
	part = MIMEBase('application', 'octet-stream')
	part.set_payload(attachment.read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	#envoie de l'email via une connexion au serveur de google
	msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email, password)
	text = msg.as_string()
	server.sendmail(email, send_to_email, text)
	server.quit()

#Connexion('127.0.0.1',12800,1,'GiveAllInfo')
