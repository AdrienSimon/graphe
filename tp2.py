
from collections import deque

class Graphe:
	def __init__(self, ordre):
		#Dictionnaire
		self.voisinSortant= {}
		#Les sommets sont 0,1,2,..., ordre-1
		self.ordre=ordre
		for sommet in range(ordre):
			self.voisinSortant[sommet]=[]
#Commentaire
	def ajouter_arc(self, debut,fin):
		#Ajoute un arc entre debut et fin
		self.voisinSortant[debut].append(fin)
	def __str__(self):
		string =""
		for i in range(self.ordre):
			string+="Voisins sortants de "
			string+=str(i)
			string+=" = "
			string+=str(self.voisinSortant[i])
			string+="\n"
		return string
	def connexe(self, sommet):
		composantes_connexe=[]
		composante_connexe=[]
		attente=[]
		attente.append(sommet)
		composante_connexe.append(sommet)
		while attente:
			courant=attente.pop()
			for i in voisinsSortant[courant]:
				attente.append(i)
#nice -n 19 python programme.python

	
def distanceEtAccess(graphe):
	for i in xrange(graphe.ordre):
		parcours_largeur(graphe,i)
		
def parcours_largeur(graphe,x):
	pred=[]
	distance=[-1 for i in xrange(graphe.ordre)]
	distance[x]=0
	fifo=deque()
	#.append()
	#.popleft()
	#.popright()
	fifo.append(x)
	while fifo:
		courant = fifo.popleft()
		for sortant in graphe.voisinSortant[courant]:
			if distance[sortant]==-1:
				distance[sortant]=distance[courant]+1
				fifo.append(sortant)
	accessible=[]
	for i in range(len(distance)):
		if distance[i]!=-1:
			accessible.append(i)
	print distance
	print "sommet accessible :"+str(accessible)
	print ("====")
	return accessible
	

	
def profondeur(graphe):
	def pp_etape(graphe,x):
		connu[x]=True
		for sortant in graphe.voisinSortant[x]:
			if connu[sortant]==False:
				connu[sortant]=True
				pred[sortant].append(x)
				pp_etape(graphe,sortant)
		numSommet.append(x)
		
		
	numSommet=[]
	connu=[False for i in xrange(graphe.ordre)]
	pred=[[] for i in xrange(graphe.ordre)]
	for i in xrange(graphe.ordre):
		if connu[i]==False:
			pp_etape(graphe,i)
	return numSommet
	

	
def lire_graphe_fichier(nom):


	compteur=0
	ordre=0
	f = open(nom, "r")
	lignes=f.readlines()
	for ligne in lignes:
		if ligne:
			mot = ligne.split()
			if len(mot)>=2 and mot[0]=="ordre":
				ordre = int(mot[1])
				nouveau=Graphe(ordre)
			if len(mot)>=3 and (mot[0]=="A" or mot[0]=="E"):
				debut = int(mot[1])
				fin = int(mot[2])
				nouveau.ajouter_arc(debut, fin)
	f.close()
	return nouveau
	
def lire_graphe_fichier2(nom):
	compteur=0
	ordre=0
	f = open(nom, "r")
	lignes=f.readlines()
	for ligne in lignes:
		if ligne:
			mot = ligne.split()
			if len(mot)>=2 and mot[0]=="ordre":
				ordre = int(mot[1])
				nouveau=Graphe(ordre)
			if len(mot)>=3 and (mot[0]=="A" or mot[0]=="E"):
				debut = int(mot[1])
				fin = int(mot[2])
				nouveau.ajouter_arc(fin, debut)
	f.close()
	return nouveau

test=lire_graphe_fichier("digraph0.txt")
profondeur(test)
print test
distanceEtAccess(test)

def fortementNaif(g):
	numeroAccess={}
	numeroComposante={}
	compteur_composante=0
	for v in xrange(g.ordre):
		numeroAccess[g.voisinSortant]=parcours_largeur(g,v)
		numeroComposante[v]
	for v1 in xrange(g.ordre):
		if numeroComposante[v1] != None:
			for v2 in xrange numeroAccess[v1]:
				if v1 in numeroAccess[v2]:
					numeroComposante[v]


#print test
#distanceEtAccess(test)



