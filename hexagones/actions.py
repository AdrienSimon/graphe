#coding: utf-8
"""
    Les actions que vous écrirez prennent en paramètre un modele. 
    Les objets manipulés sont :
        - les sommets (visuellement, les cases hexagonales). 
             (Les sommets sont des objets 'Hex' mais 
             vous n'avez pas besoin de les manipuler directement,
             seulement de les passer en paramètre.)

        - les flèches 
            (même remarque que pour les sommets 
            ce sont en fait des entiers qui representent des objets manipulés
            par la bibliothèque graphique Tkinter)
    
    Les methodes de l'objet modele utilisables sont les suivantes :

    ### METHODES LIEES AU MODELE THEORIQUE #########################

    modele.getListeSommets():
        renvoie la liste des sommets du modele. 
        Rq : modele.getListeSommets(True) renvoie la liste de tous les
        sommets même noirs

    modele.getDepart():
        renvoie le sommet de départ

    modele.getObjectif(self):
        renvoie le sommet objectif

    modele.getVoisins(self, sommet):
        renvoie la liste des sommets voisins d'un sommet donné.
        Rq : modele.getVoisins(True) renvoie la liste de tous les
        voisins même noirs

    modele.longueur(sommet1, sommet2):
        renvoie la longueur de l'arete entre ces deux sommets
        configurable en changeant les valeurs dans hexa_modele

    ### METHODES GRAPHIQUES #########################
    
    modele.addFleche(sommet1, sommet2, couleur): 
        ajoute une fleche du sommet 1 au sommet 2, de la couleur donnée,
        et renvoie un indentifiant (un entier) qui permet de la supprimer plus tard
        couleurs : "Black", "Red", etc.

    model.delFleche(ref):
        supprimer la fleche dont l'identifiant est ref

    modele.addTexte(sommet, texte):
        ajoute un texte sur le sommet donne. Renvoie un identifiant pour 
        pouvoir le supprimer.
        
    modele.deltexte(ref):
        suppprime le texte dont l'identifiant est ref.

    modele.update()
        met a jour l'affichage

"""



from hexa_modele import *
import random
import time
from collections import deque

def parcoursEnLargeur(modele):
    distance = {}
    distance[modele.getDepart()] = 0
    predecesseur = {}
    fifo = deque([modele.getDepart()])
    finished = False
    while fifo and not finished:
        courant = fifo.pop()
        if courant == modele.getObjectif():
            finished = True
        for voisin in modele.getVoisins(courant):
            if voisin not in distance:
                distance[voisin] = distance[courant] + 1
                predecesseur[voisin] = courant
                fifo.appendleft(voisin)
                modele.addTexte(voisin, distance[voisin])
                modele.addFleche(courant, voisin, 'Grey')
                modele.observateur.update()
                time.sleep(0.5)
    if modele.getObjectif() in predecesseur:
        courant = modele.getObjectif()
        while courant != modele.getDepart():
            modele.addFleche(predecesseur[courant], courant, 'Red')
            courant = predecesseur[courant]

def bellmanFord(modele):
    distance = {}
    predecesseur = {}
    fleche = {}
    distance[modele.getDepart()] = 0
    for i in xrange(len(modele.getListeSommets())):
        operationsEffectuees = False
        for s1 in modele.getListeSommets():
            for s2 in modele.getVoisins(s1):
                if (s1 in distance and s2 not in distance) or (s1 in distance and s2 in distance and distance[s1] + modele.longueur(s1, s2) < distance[s2]):
                    operationsEffectuees = True
                    distance[s2] = distance[s1] + modele.longueur(s1, s2)
                    predecesseur[s2] = s1
                    modele.deltexte(s2)
                    modele.addTexte(s2, distance[s2])
                    if s2 in fleche:
                        modele.delFleche(fleche[s2])
                    fleche[s2] = modele.addFleche(s1, s2, 'Grey')
                    modele.observateur.update()
                    time.sleep(0.01)
        if not operationsEffectuees:
            break
    if modele.getObjectif() in predecesseur:
        courant = modele.getObjectif()
        while courant != modele.getDepart():
            modele.addFleche(predecesseur[courant], courant, 'Red')
            courant = predecesseur[courant]

def dijkstra(modele): 
    fleche = {}
    distance = {}
    distance[modele.getDepart()] = 0
    termine = {}
    predecesseur = {}
    filePriorite = {}
    filePriorite[modele.getDepart()] = 0
    finished = False
    while filePriorite and not finished:
        courant = filePriorite.keys()[filePriorite.values().index(min(filePriorite.values()))]
        del filePriorite[courant]
        for voisin in modele.getVoisins(courant):
            if voisin == modele.getObjectif():
                finished = True
            if voisin not in termine:
                if (courant in distance and voisin not in distance) or (courant in distance and voisin in distance and distance[courant] + modele.longueur(courant, voisin) < distance[voisin]):
                    distance[voisin] = distance[courant] + modele.longueur(courant, voisin)
                    modele.deltexte(voisin)
                    modele.addTexte(voisin, distance[voisin])
                    if voisin in fleche:
                        modele.delFleche(predecesseur[voisin], voisin)
                    predecesseur[voisin] = courant
                    modele.addFleche(courant, voisin, 'Grey')
                    modele.observateur.update()
                    time.sleep(0.01)
                    filePriorite[voisin] = distance[voisin]
        termine[courant] = True
    if modele.getObjectif() in predecesseur:
        courant = modele.getObjectif()
        while courant != modele.getDepart():
            modele.addFleche(predecesseur[courant], courant, 'Red')
            courant = predecesseur[courant]

def astar(modele): 
    def h():
        distance = {}
        distance[modele.getObjectif()] = 0
        fifo = deque()
        fifo.appendleft(modele.getObjectif())
        while fifo:
            courant = fifo.pop()
            for voisin in modele.getVoisins(courant, True):
                if voisin not in distance:
                    distance[voisin] = distance[courant] + 1
                    fifo.appendleft(voisin)
        return distance
    dh = h()
    fleche = {}
    distance = {}
    distance[modele.getDepart()] = 0
    termine = {}
    predecesseur = {}
    filePriorite = {}
    filePriorite[modele.getDepart()] = 0
    finished = False
    while filePriorite and not finished:
        courant = filePriorite.keys()[filePriorite.values().index(min(filePriorite.values()))]
        del filePriorite[courant]
        for voisin in modele.getVoisins(courant):
            if voisin == modele.getObjectif():
                finished = True
            if voisin not in termine:
                if (courant in distance and voisin not in distance) or (courant in distance and voisin in distance and distance[courant] + modele.longueur(courant, voisin) - dh[courant] + dh[voisin] < distance[voisin]):
                    distance[voisin] = distance[courant] + modele.longueur(courant, voisin) - dh[courant] + dh[voisin]
                    modele.deltexte(voisin)
                    modele.addTexte(voisin, distance[voisin])
                    if voisin in fleche:
                        modele.delFleche(predecesseur[voisin], voisin)
                    predecesseur[voisin] = courant
                    modele.addFleche(courant, voisin, 'Grey')
                    modele.observateur.update()
                    time.sleep(0.01)
                    filePriorite[voisin] = distance[voisin]
        termine[courant] = True
    if modele.getObjectif() in predecesseur:
        courant = modele.getObjectif()
        while courant != modele.getDepart():
            modele.addFleche(predecesseur[courant], courant, 'Red')
            courant = predecesseur[courant]
   
