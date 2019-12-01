import socket
import psutil

def dec2bin(dec): #convertit decimal vers binaire, rajoute des '0' pour retourner 8 bits #a Théo
    return "0"* (8-len("{0:b}".format(dec) ) ) +"{0:b}".format(dec)

def bin2dec(b): #trouver sur internet
	i=0
	n=len(b)
	puissance=0
	index=-1
	while index>=-n:
		if b[index]=='1':
			i= i + 2**puissance
		elif b[index]!='0' :
			return None
		puissance= puissance +1
		index=index-1
	return i

def InverseAdresse(TableauAdresseBinaire):#permet d'inverser l'orientation d'une adresse 
	InverTabNetworkMask=[]
	DeuxInverTabNetworkMask=[]

	for i in reversed(TableauAdresseBinaire): #inverse une premiere fois l'adresse diviser en 4 bloc binaire
		InverTabNetworkMask.append(i)

	for i in range(0,4):
		for x in reversed(InverTabNetworkMask[i]): #inverse chaque bloc de l'adresse a inverser
			DeuxInverTabNetworkMask.append(x)

	return DeuxInverTabNetworkMask #retourne l'adresse inverser en un bloc


def RecupPool(AdressePC,NetworkMask):
	TabAdressePC=[]
	CompteurBits=0
	TabNetworkMask=[]
	FinalPool=[]

	SplitAdressePC=AdressePC.split(".") #Découpage de l'adresse ip dans un tableau a 4 cases
	for i in range(0,4):
		TabAdressePC.append(dec2bin(int(SplitAdressePC[i]))) #conversion de l'adresse ip en binaire

	SplitNetworkMask=NetworkMask.split(".") #Découpage de du masque réseau dans un tableau a 4 cases
	for i in range(0,4):
		TabNetworkMask.append(dec2bin(int(SplitNetworkMask[i]))) #conversion de du masque de réseau en binaire

	MaskInverser=InverseAdresse(TabNetworkMask) #inversion du masque afin de compter le nombre de 0 du masque afin de connaitre combien de bits sont variable sur l'adresse ip réseau

	for i in range(0,len(MaskInverser)): #compte de nombre de bits variable de l'adresse ip
		if MaskInverser[i]!=str(1):
			CompteurBits=CompteurBits+1
		else:
			break


	TabAdressePC="".join(TabAdressePC) #Obtentions de l'adresse ip binaire en un bloc
	
	#détermine le pool d'adressage du réseau
	for i in range(1,bin2dec(str(1)*CompteurBits)): #determine le nombre décimale de la partie variable avant d'être convertie en binaire
		partVarBinaireIncomplete=dec2bin(i) #obtention de la partie variable en binaire
		PartVariableComplete=str(0)*(CompteurBits-len(partVarBinaireIncomplete))+partVarBinaireIncomplete #comble la partie variable par des 0 si besoin
		FinalAdresse=TabAdressePC[:31-CompteurBits]+PartVariableComplete #détermine l'une des adresse du pool en un bloc binaire
		FinalAdresse=str(bin2dec(FinalAdresse[:8]))+"."+str(bin2dec(FinalAdresse[8:16]))+"."+str(bin2dec(FinalAdresse[16:24]))+"."+str(bin2dec(FinalAdresse[24:32])) #découpage de l'adresse du pool en plusieurs bloc binaire afin de convertir les blocs en decimale est donc d'avoir l'une des adresses du pool
		FinalPool.append(FinalAdresse)#remplisage du table contenant le pool d'adresse qui va être retourné
	
	return FinalPool


def recupMask():
	AllAddress=[]
	AllInterface=[]
	for i in psutil.net_if_addrs():
		AllInterface.append(i)
		AllAddress.append(psutil.net_if_addrs()[i][0].address)


	ActuelAddress=socket.gethostbyname(socket.gethostname())

	for i in range(0,len(AllAddress)):
		if AllAddress[i]==ActuelAddress:
			NameInterface=AllInterface[i]
			break

	return psutil.net_if_addrs()[NameInterface][0].netmask

def PoolAPing():
	return RecupPool(socket.gethostbyname(socket.gethostname()),recupMask())

