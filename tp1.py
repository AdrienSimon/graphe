import copy
global vu
vu=[]
class Etat:
	def __init__(self,cases):
		self.cases=cases
		self.voisins=[]



premier = Etat([[6,4,1],[7,3,8],[2,5,None]])
dernier = Etat([[1,2,3],[4,5,6],[7,8,None]])
vu.append(premier.cases)
#print premier.cases

def chercher_voisins(etat_initial):
	test=True
	global vu
	for i in range(3):
		for j in range(3):
			if etat_initial.cases[i][j]==None: #Chercher la case vide
				for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]: #parcours des voisins de la case vide
					vi=i+di
					vj=j+dj
					if 0<=vi<3 and 0<=vj<3:  # Verif que la case existe
						#print vi,vj
						nouveau=copy.deepcopy(etat_initial.cases)
						nouveau[i][j]=nouveau[vi][vj]
						nouveau[vi][vj]=None
						#print nouveau
						for z in range(len(vu)):
							#print z
							#print vu[z]
							#print nouveau
							if vu[z]==nouveau:
								test=False
						if test:
							print "ajout"
							etat_initial.voisins.append(Etat(nouveau))
							vu.append(nouveau)
	for i in rabge(len(vu)):
		if 

chercher_voisins(premier)















# 1 2 3
# 4 0 5
# 6 7 8

