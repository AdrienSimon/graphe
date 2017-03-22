#coding: utf-8
import random    
import math

class Grille_modele(object):

    def __init__(self, observateur, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.hexs = {}  # dictionnaire de (coordonnees : Hex)
        self.observateur = observateur
        self.hexs = {}  # dictionnaire de (coordonnees : Hex)
        for x in range(self.largeur):
            for y in range(self.hauteur):
                self.hexs[(x,y)] = Hex(x, y, self.observateur)
        self.depart = self.hexs[(0,self.hauteur-1)]
        self.depart.change_couleur("Magenta")
        self.objectif = self.hexs[(self.largeur-1,0)]
        self.objectif.change_couleur("Red")
   
    def evaldistance(self,sommet1, sommet2,):
        return int(max(math.fabs(sommet1.x-sommet2.x),
                 math.fabs(sommet1.y-sommet2.y))) 
   

    def reset(self):
        for key,hex in self.hexs.items():
            hex.change_couleur("White", False)
        self.depart.change_couleur("Magenta")
        self.objectif.change_couleur("Red")

       

    def addFleche(self, sommet1, sommet2, couleur):
        return self.observateur.add_arrow(sommet1.x, sommet1.y, sommet2.x, sommet2.y, couleur)

    def delFleche(self, ref):
        self.observateur.delete(ref)

    def deltexte(self, ref):
        self.observateur.delete(ref)

    def addTexte(self, sommet, texte):
        return self.observateur.add_text(sommet.x, sommet.y, texte)

    def getListeSommets(self, tous=False):
        liste = []
        for key, value in self.hexs.items():
            if tous or value.couleur != "Black":
                liste.append(value)
        return liste

    def getDepart(self):
        return self.depart

    def getObjectif(self):
        return self.objectif

    def notify(self, message):
        self.observateur.miseAJour(message)

    def getVoisins(self, sommet, tous=False):
        #renvoie la liste des voisins par coordonnees
        vois = []
        for u,v in ( (-1,-1 + sommet.x%2), (-1,0 + sommet.x%2), (1,-1 + sommet.x%2), (1,0 + sommet.x%2), (0,-1), (0,1)):
            xv = sommet.x + u 
            yv = sommet.y + v
            if self.hexs.has_key((xv, yv)):
               if tous or self.hexs[(xv, yv)].couleur != "Black":
                    vois.append(self.hexs[(xv, yv)])
        return vois


    def change_objectif(self, nouvelObjectif):
        self.objectif.change_couleur("White")
        self.objectif = self.hexs[nouvelObjectif]
        self.objectif.change_couleur("Red")


    def change_depart(self, nouveauDepart):
        self.depart.change_couleur("White")
        self.depart = self.hexs[nouveauDepart]
        self.depart.change_couleur("Magenta")

    def random(self):
        couleurs = ["White", "Blue", "Green", "Yellow", "Black"]
        for key, hex in self.hexs.items():
            if hex != self.depart and hex != self.objectif:
                hex.change_couleur(couleurs[random.randint(0,4)])


    def longueur(self, sommet1, sommet2):
        """calcule la longueur de l'arête entre deux sommets voisins suivant leur couleur.
        A chaque couleur est associée un cout.
        la distance est alors (cout1 + cout2) / 2 """
        couts = {"White" : 1,
                 "Blue" : 10,
                 "Green" : 5,
                 "Yellow" : 2,
                 "Red" : 1,
                 "Magenta" : 1}
        return (couts[sommet1.couleur]+couts[sommet2.couleur])/2

    def update():
        self.observateur.update()

class Hex(object):
    def __init__(self, x, y, observateur):
        self.text = ""
        self.couleur = "White"
        self.x = x
        self.y = y
        self.observateur = observateur



    def change_couleur(self, couleur, notify = True):
        self.couleur = couleur
        parametres = {"x": self.x, "y": self.y, "type" : "couleur", "arg" : self.couleur}
        if notify:
            self.notify(parametres)

    def notify(self, parametres):
        self.observateur.miseAjour(parametres)



