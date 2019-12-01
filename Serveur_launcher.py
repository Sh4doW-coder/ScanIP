# -*- coding: utf-8 -*-

import Serveur	#On fait appel aux fonctions présentes dans Serveur.py
from tkinter import *
from threading import Thread



def ReponseServeur(): #Menu correspondant au choix de scanner l'ensemble du réseau local

	window2 = Tk()
	window2.title("Serveur Etat")
	window2.geometry('400x30')

	LegendZonedetexte3 = Label(window2, text="Le serveur écoute sur le port que vous avez préciser").pack()

	window2.mainloop()


def propos():
	window3 = Tk()
	window3.title("Serveur")
	window3.geometry("480x160")

	LegendZonedetexte2 = Label(window3, text='''Bienvenue sur la partie Serveur de ScanIP, ici
		Vous pourez paramétrer le port sur lequels écoute le serveur afin d\'envoyer des donners au clients.''').pack()

	window3.mainloop()



window = Tk()
window.title("Serveur")
window.geometry("500x80")

zoneTexte1 = Entry(window,width=10)
LegendZonedetexte2 = Label(window, text="Veuillez renseiller un Port pour contacter le serveur").pack()
zoneTexte1.pack()

def Pop():
	port = [int( zoneTexte1.get() )] #args est une liste d'argument sinon erreur
	th1= Thread(target=Serveur.lanceServeur, args=(port))
	th1.start()
	ReponseServeur()

window.bind('<Return>', Pop)
btn = Button(window, text="Ecoute", command=Pop)
btn.pack()


barre_menu = Menu(window)

onglet_aide = Menu(barre_menu, tearoff=0)
onglet_aide.add_command(label="A propos", command=propos)
onglet_aide.add_command(label="Fermer", command=window.destroy)
barre_menu.add_cascade(label="Aide", menu=onglet_aide)


window.config(menu=barre_menu)


window.mainloop()
