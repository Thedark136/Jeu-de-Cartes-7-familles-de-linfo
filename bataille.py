
from tkinter import *
from random import shuffle

les_cartes = {
    "Sécurité et confidentialité":[("Jules César",1),("AL-Kindi",2),("Diffie Hellman",3),("Rivest-Shamir-Adleman (RSA)",4),("Shafi Goldwasser",5),("Cynthia Dwork",6)],
    "Algorithmes & Programmation":[("Al-Khwarizmi",1), ("Ada Lovelace",2), ("Grace Hopper",3), ("Dorothy Vaughan",4), ("Gilles Kahn",5), ("Gérard Berry",6)],
    "Mathématiques & Informatique":[("Hypatie d'Alexandrie",1), ("George Boole",2), ("Alonzo Church",3), ("Jacques-Louis Lions",4), ("Ingrid Daubechies",5), ("Jocelyne Troccaz",6)],
    "Intelligence Artificielle":[("Herbert Simon",1), ("Marvin Minsky",2), ("Geoffrey Hinton",3), ("Rose Dieng-Kuntz",4), ("Yann LeCun",5), ("Cordelia Schmid",6)],
    "Machines & Composants":[("Charles Babbage",1), ("John von Neumann",2), ("Hedy Lamarr",3), ("Seymour Cray",4), ("Gordon Moore",5), ("Hiroshi Ishiguro",6)],
    "Interaction Homme-Machine":[("Doug Engelbart",1), ("Ted Nelson",2), ("Alan Kay",3), ("Joëlle Coutaz",4), ("Jean-Marie Hullot",5), ("Marie-Paule Cani",6)],
    "Systèmes & réseaux":[("Alexander Graham Bell",1), ("Claude Shannon",2), ("Vinton Cerf",3), ("Tim Berners-Lee",4), ("Pascale Vicat-Blanc",5), ("Anne-Marie Kermarrec",6)],
    "Joker":[("Alan Turing",7),("Alan Turing",7)]
}


def cards(cartes):
    mes_cartes = []
    for elt in cartes:
        for j in range(len(cartes[elt])):
            mes_cartes.append(cartes[elt][j])
    return mes_cartes

def mélanger(cartes):
    mes_cartes = cards(cartes)
    shuffle(mes_cartes)
    return mes_cartes

def distribuer(cartes):
    joueur_1 = []
    joueur_2 = []
    for i in range (0,len(cartes),2):
        joueur_1.append(cartes[i])
        joueur_2.append(cartes[i+1])
    return joueur_1, joueur_2

def bataille(cartes):
    cartes_mélangées = mélanger(cartes)
    joueur_1, joueur_2 = distribuer(cartes_mélangées)
    print(joueur_1, joueur_2)
    
    while len(joueur_1)!=0 and len(joueur_2)!=0:
        if joueur_1[0]>joueur_2[0]:
            print("Joueur 1 gagne la manche")
            joueur_1.append(joueur_2[0])
            joueur_1.append(joueur_1.pop(0))
            del joueur_2[0]
        elif joueur_2[0]>joueur_1[0]:
            print("Joueur 2 gagne la manche")
            joueur_2.append(joueur_1[0])
            joueur_2.append(joueur_2.pop(0))
            del joueur_1[0]
        else:
            print("égalité")
            joueur_1.append(joueur_1.pop(0))
            joueur_2.append(joueur_2.pop(0))
    if len(joueur_1)==0:
        return ("Joueur 2 a gagné le match")
    else:
        return("Joueur 1 a gagné le match")

print(bataille(les_cartes))