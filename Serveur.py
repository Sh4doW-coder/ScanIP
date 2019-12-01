# -*- coding: utf-8 -*-

import socket
import platform
import getpass
import psutil

def lanceServeur(Nport):
	hote = ''
	port =  int(Nport)

	connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connexion_principale.bind((hote, port))
	connexion_principale.listen(5)

	def servv():

		print("Le serveur écoute à présent sur le port {}".format(port))
		
		connexion_avec_client, infos_connexion = connexion_principale.accept()

		infotest=[]
		
		for proc in psutil.process_iter():
			infotest=proc

		r = ("Serveur "+connexion_avec_client.getsockname()[0]+' '+"OS : "+platform.platform()+' '+"Utilisateur : "+getpass.getuser()).encode()
		connexion_avec_client.send(r)

		print("Fermeture de la connexion")
		connexion_avec_client.close()

	
	while True:
		servv()