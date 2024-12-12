from math import *
from random import *
from time import *
from doctest import *

VIDE = 0
THON = 1
REQUIN = 2

def genere_grille_vide(n):
    """
    Crée une grille vide de dimension nxn remplie de zéros.
    :param n: (int) taille de la grille
    :return: (list) grille de taille nxn avec tous les éléments égaux à 0
    """
    tableau = [[0 for j in range(n)] for i in range(n)]
    return tableau

def affiche_grille(grille):
    '''
    Affiche dans la console la grille wa-tor passée en paramètre. 
    :param grille: (list) liste de liste de même taille
    :CU: len(grille)==len(grille[0])==len(grille[1])==...
    :return: None
    :effet de bord: affiche la grille dans la console
    >>> affiche_grille([[0, 0], [0, 0]])
    0 0 
    0 0 
    '''
    for i in grille:
        print()
        for j in i:
            print(j, end=' ')

def remplir_grille(grille_vide):
    '''
    Rempli et renvoie une grille vide de dimension nxn avec 30% de THON (représenté par des 1)
    et 10% de REQUINS (représenté par des 2).
    :param grille_vide: (list) grille wa-tor vide
    :return: (list) grille wa-tor remplie
    '''
    dim = len(grille_vide)
    nb_thon = int(dim * dim * 0.30)
    
    nb_requin = ceil(dim * dim * 0.10)

    while nb_thon > 0:
        x = randrange(dim)
        y = randrange(dim)
        if grille_vide[x][y] == VIDE:
            grille_vide[x][y] = THON
            nb_thon -= 1
            
    while nb_requin > 0:
        x = randrange(dim)
        y = randrange(dim)
        if grille_vide[x][y] == VIDE:
            grille_vide[x][y] = REQUIN
            nb_requin -= 1

    return grille_vide

def est_thon(grille, x, y):
    if grille[x][y] == THON:
        return True
    return False

def est_requin(grille, x, y):
    if grille[x][y] == REQUIN:
        return True
    return False


def liste_voisin(grille, x, y, cible):

    dim = len(grille)
    voisins = []
    
    directions = [
        (-1, 0),  
        (1, 0),  
        (0, -1),  
        (0, 1)   
    ]
    
    for dx, dy in directions:
        vx = (x + dx) % dim
        vy = (y + dy) % dim
        
        if grille[vx][vy] == cible:
            voisins.append((vx, vy))
    
    return voisins

def deplacement(grille, x_depart, y_depart, x_arrivee, y_arrivee):
    valeur_depart = grille[x_depart][y_depart]
    grille[x_arrivee][y_arrivee] = valeur_depart
    grille[x_depart][y_depart] = VIDE
    return grille

def deplacement_thon(grille, x, y):
    if not est_thon(grille, x, y):
        return grille
    voisins_vides = liste_voisin(grille, x, y, VIDE)
    if not voisins_vides:
        return grille
    x_arrivee, y_arrivee = voisins_vides[randrange(len(voisins_vides))]
    grille = deplacement(grille, x, y, x_arrivee, y_arrivee)
    return grille

def deplacement_requin(grille, x, y):
    if not est_requin(grille, x, y):
        return grille
    voisins_thon = liste_voisin(grille, x, y, THON)
    if voisins_thon:
        x_arrivee, y_arrivee = voisins_thon[randrange(len(voisins_thon))]
        grille = deplacement(grille, x, y, x_arrivee, y_arrivee)
    else:
        voisins_vides = liste_voisin(grille, x, y, VIDE)
        if voisins_vides:
            x_arrivee, y_arrivee = voisins_vides[randrange(len(voisins_vides))]
            grille = deplacement(grille, x, y, x_arrivee, y_arrivee)
    return grille

def evolution(grille):
    dim = len(grille)
    cases_non_vides = []
    for i in range(dim):
        for j in range(dim):
            if grille[i][j] != VIDE:
                cases_non_vides.append((i, j))
    if cases_non_vides:
        x, y = cases_non_vides[randrange(len(cases_non_vides))]
        if est_thon(grille, x, y):
            grille = deplacement_thon(grille, x, y)
        elif est_requin(grille, x, y):
            grille = deplacement_requin(grille, x, y)
    return grille

def wator(n, p):
    grille_vide = genere_grille_vide(n)
    grille = remplir_grille(grille_vide)
    for i in range(p):
        affiche_grille(grille)
        print("\n--- Evolution étape", i + 1, "---")
        sleep(1)
    
        grille = evolution(grille)


