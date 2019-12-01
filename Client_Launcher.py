# -*- coding: utf-8 -*-

import socket
import Client	#On fait appel aux fonctions présentes dans Client.py
import os
import PoolAdresse
from tkinter import *
import os
import webbrowser

window = Tk()
window.title("Client")
window.geometry("480x360")
window.minsize(200, 400)
window.maxsize(800, 600)



def ScanAuto(): #Menu correspondant au choix de scanner l'ensemble du réseau local

	window2 = Tk()
	window2.title("Scan IP")
	window2.geometry('400x400')

	zoneTexte1 = Entry(window2,width=10)
	LegendZonedetexte2 = Label(window2, text="Veuillez renseiller un Port").pack()
	zoneTexte1.pack()

	zoneTexte2 = Entry(window2,width=10)
	LegendZonedetexte3 = Label(window2, text="Veuillez renseiller un temps de TimeOut").pack()
	zoneTexte2.pack()

	def clicked(*argv):
		port = int( zoneTexte1.get() )
		timeout = float( zoneTexte2.get() )
		Client.ScanAuto(port,timeout)
	window2.bind('<Return>', clicked)
	
	btn = Button(window2, text="Connexion", command=clicked)
	btn.pack()
	window2.mainloop()

def Afficher_Form_Email(): #Fenêtre pour que l'utilisateur entre l'adresse mail où seront envoés les donnéees

	window2 = Tk()
	window2.title("Envoi du resultat par Email")
	window2.geometry('400x400')

	zoneTexte1 = Entry(window2,width=50)
	LegendZonedetexte2 = Label(window2, text="Veuillez renseiller une adresse email").pack()
	zoneTexte1.pack()

	def clicked(*argv):
		Email = str( zoneTexte1.get() )
		Client.EnvoieEmail(Email)
	window2.bind('<Return>', clicked)
	
	btn = Button(window2, text="Envoie", command=clicked)
	btn.pack()
	window2.mainloop()










def ScanIp(): #Menu correspondant au choix de scanner une adresse IP que l'utilisateur va entrer manuellement

	window2 = Tk()
	window2.title("Scan IP")
	window2.geometry('400x400')

	zoneTexte1 = Entry(window2,width=10)
	LegendZonedetexte2 = Label(window2, text="Veuillez renseiller un Port").pack()
	zoneTexte1.pack()

	zoneTexte2 = Entry(window2,width=10)
	LegendZonedetexte3 = Label(window2, text="Veuillez renseiller un temps de TimeOut").pack()
	zoneTexte2.pack()

	zoneTexte3 = Entry(window2,width=10)
	LegendZonedetexte = Label(window2, text="Veuillez renseiller une adresse IP").pack()
	zoneTexte3.pack()

	def clicked(*argv):
		port = int( zoneTexte1.get() )
		timeout = int( zoneTexte2.get() )
		ip = zoneTexte3.get()
		Client.ScanIp(port,timeout,ip)
	window2.bind('<Return>', clicked)

	btn = Button(window2, text="Connexion", command=clicked)
	btn.pack()
	window2.mainloop()


def OuvrirLog():
	webbrowser.open("connexions.log")








def ScanCSV(): #Afficher la fenêtre relative au choix de l'importation d'un fichier CSV comme source de donnéees pour les adresses à scanner
	from tkinter.filedialog import askopenfilename
	fichier = askopenfilename()
	
	window2 = Tk()
	window2.title("CSV")
	window2.geometry('400x400')
	
	
	

	zoneTexte1 = Entry(window2,width=10)
	LegendZonedetexte2 = Label(window2, text="Veuillez renseiller un Port").pack()
	zoneTexte1.pack()

	zoneTexte2 = Entry(window2,width=10)
	LegendZonedetexte3 = Label(window2, text="Veuillez renseiller un temps de TimeOut").pack()
	zoneTexte2.pack()

	
	LegendZonedetexte = Label(window2, text=fichier).pack()
	

	def Open():
		port = int( zoneTexte1.get() )
		timeout = int( zoneTexte2.get() )
		Client.ScanCSV(fichier,port,timeout)

	btn = Button(window2, text="Connexion", command=Open)
	btn.pack()
	window2.mainloop()





def manuel(): #Fenêtre relative au guide d'utilisation
	window = Tk()
	window.title("Manuel d'utilisation")
	window.geometry("560x320")
	Label(window, text="""-Pour se connecter à un serveur précis cliquez sur 'connexion' puis 'entrer une adresse IP'\n\n
	-Pour se connecter à plusieurs serveurs dont les adresses IP sont présentes dans un fichier CSV:\n
	Il suffit d'importer le fichier CSV et de rentrer le port d'écoute et le timeout.\n\n
	-Si vous n'avez aucune information vous pouvez utiliser le scan automatique:\n
	Il suffit d'entrer les mêmes informations que pour l'importation de fichiers CSV
	
	
	""").pack()
	
	window.mainloop()
	
def apropos(): #Fenêtre relative au informations à propos du programme
	def RAYAN():
		webbrowser.open('http://www.python.org')
	def THEO():
		webbrowser.open('https://github.com/Divulgacheur')
	def AYMERIC():
		webbrowser.open('https://de-sousa-aymeric.hubside.fr/')
	window = Tk()
	window.title("A propos")
	window.geometry("480x360")
	Label(window, text="""Cette application a été réalisé par Rayan BENLACHEHEB, Théo PELTIER et Aymeric DE SOUSA
	
	
	""").pack()
	btn = Button(window, text="Site Rayan", command=RAYAN)
	btn.pack()
	
	btnA = Button(window, text="Site Théo", command=THEO)
	btnA.pack()
	
	btnB = Button(window, text="Site Aymeric", command=AYMERIC)
	btnB.pack()
	
	
	window.mainloop()







def fenetre_principale():
	barre_menu = Menu(window) #création d'une barre verticale où se trouveront différents onglets

	onglet_connexion = Menu(barre_menu, tearoff=0)
	onglet_connexion.add_command(label="Entrer une addresse IP", command=ScanIp)
	onglet_connexion.add_command(label="Scan automatique", command=ScanAuto)
	onglet_connexion.add_command(label="Importer fichier CSV", command=ScanCSV)
	onglet_connexion.add_separator()
	onglet_connexion.add_command(label="Quitter", command=window.destroy)
	barre_menu.add_cascade(label="Connexion", menu=onglet_connexion)


	onglet_historique= Menu(barre_menu, tearoff=0)
	onglet_historique.add_command(label="Afficher l'historique des connexions", command=OuvrirLog)
	onglet_historique.add_command(label="Envoyer par mail", command=Afficher_Form_Email)
	barre_menu.add_cascade(label="Historique", menu=onglet_historique)

	onglet_aide = Menu(barre_menu, tearoff=0)
	onglet_aide.add_command(label="A propos", command=apropos)
	onglet_aide.add_command(label="Manuel", command=manuel)
	barre_menu.add_cascade(label="Aide", menu=onglet_aide)

	window.config(menu=barre_menu)




	window.mainloop()


fenetre_principale()
