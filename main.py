#     _   _______ ____   _____
#    / | / / ___//  _/  |__  /
#   /  |/ /\__ \ / /     /_ < 
#  / /|  /___/ // /    ___/ / 
# /_/ |_//____/___/   /____/  

# on import les librairy pour le ui et le jeu
from tkinter import *
import random
from PIL import Image, ImageTk
import time

root = Tk()
root.title('Nsi Project 3')
#la aspect ratio de la fenetre
root.geometry("1000x550")
#la couleur de la background
root.configure(background="#F5F1ED")

#les cartes des 7 familles avec chacune leur puissance
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

# fonction qui prend toutes les cartes et ranges les dans une liste
def cards(cartes):
    mes_cartes = []
    for elt in cartes:
        for j in range(len(cartes[elt])):
            mes_cartes.append(cartes[elt][j])
    return mes_cartes

def mélanger(cartes):
    mes_cartes = cards(cartes)
    random.shuffle(mes_cartes)
    return mes_cartes

# fonction pour initialiser la photo du deriere des cartes au debut du program
def init():
    global joueur1_image
    joueur1_image = resize_cards(f'Cartes/back.png')
    joueur1_label.config(image=joueur1_image)

    global joueur2_image
    joueur2_image = resize_cards(f'Cartes/back.png')
    joueur2_label.config(image=joueur2_image)



# Redimensionner les cartes
def resize_cards(card):
	# Ouvrir l'image
	our_card_img = Image.open(card)
	# Redimensionner l'image
	our_card_resize_image = our_card_img.resize((150, 218))
	# sortir la carte
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)
	# Renvoyez cette carte
	return our_card_image



# fonctions pour commencer le jeux
def commencer():
    # on melange le cartes pour les preparer a diffuser au 2 joueurs
    cartes = mélanger(les_cartes)
    global joueur_1
    global joueur_2
    joueur_1 = []
    joueur_2 = []
    #une loop por distribuer les cartes melanger
    for i in range (0,len(cartes),2):
        joueur_1.append(cartes[i])
        joueur_2.append(cartes[i+1])
    #changer le button pour demande le rejouement
    commence_button.config(text="Rejouer")


def Jouer():
    #initialisation des nombre de victoire
    joueur_1_victoire = 0
    joueur_2_victoire = 0
    #n chnage le tittre de la window pour dire le nombre de victoire
    root.title(f'Projet NSI 3 - Victoires du Joueur 1 : {joueur_1_victoire}, Victoires du Joueur 2: {joueur_1_victoire}')
	# on voit qui gagne 
    if len(joueur_1)==0:
        joueur_2_victoire+=1
        root.title(f'Projet NSI 3 - Victoires du Joueur 1 : {joueur_1_victoire}, Victoires du Joueur 2: {joueur_1_victoire}')
        return ("Joueur 2 a gagné le match")
    
    elif len(joueur_2)==0:
        joueur_1_victoire+=1
        root.title(f'Projet NSI 3 - Victoires du Joueur 1 : {joueur_1_victoire}, Victoires du Joueur 2: {joueur_1_victoire}')
        return("Joueur 1 a gagné le match")
    
    #on compare les cartes et donne les 2 cartes au gagnent
    # sauf si c'est une egalite
    if joueur_1[0][1]>joueur_2[0][1]:
        print("Joueur 1 gagne la manche")
        joueur_1.append(joueur_2[0])
        joueur_1.append(joueur_1.pop(0))
        del joueur_2[0]
    
    elif joueur_2[0][1]>joueur_1[0][1]:
        print("Joueur 2 gagne la manche")
        joueur_2.append(joueur_1[0])
        joueur_2.append(joueur_2.pop(0))
        del joueur_1[0]
    else:
        print("égalité")
        joueur_1.append(joueur_1.pop(0))
        joueur_2.append(joueur_2.pop(0))
    
    #on affice le nombre de cartes
    joueur1_frame.config(text=f"Joueur 1 - Cartes :  {len(joueur_1)}")
    joueur2_frame.config(text=f"Joueur 2 - Cartes :  {len(joueur_2)}")
    
    # on affiche les images prochaine au user
    global joueur1_image
    joueur1_image = resize_cards(f'Cartes/{joueur_1[0][0]}.png')
    joueur1_label.config(image=joueur1_image)
    
    global joueur2_image
    joueur2_image = resize_cards(f'Cartes/{joueur_2[0][0]}.png')
    joueur2_label.config(image=joueur2_image)
    



#on travail toujours sur une fonction pour automatiser le jeu mais il
# y a des problem avec laffiche des images

#dangerzone: se code crash le program !ne pas utiliser!
# def Jouer_loop():
#     while joueur_1 != 0 and joueur_2 != 0:
#         Jouer()
#         time.sleep(0.001)
#dangerzone

my_frame = Frame(root, bg="#F5F1ED")
my_frame.pack(pady=20)

# Créer des cadres pour les cartes
joueur1_frame = LabelFrame(my_frame, text="Player 1" , fg='white', bd=0, bg="#252323")
joueur1_frame.grid(row=0, column=0, padx=20, ipadx=30)

joueur2_frame = LabelFrame(my_frame, text="Player 2" , fg='white', bd=0, bg="#252323")
joueur2_frame.grid(row=0, column=1, ipadx=30)

# Mettre les cartes dans des cadres
joueur1_label = Label(joueur1_frame, text='')
joueur1_label.pack(pady=20)

joueur2_label = Label(joueur2_frame, text='')
joueur2_label.pack(pady=20)


# Créer un bouton pour démarrer le jeu et jouer aux cartes
commence_button = Button(root, text="Commencer", font=("Helvetica", 14), command=commencer)
commence_button.pack(pady=10)

jouer_button = Button(root, text="Jouer", font=("Helvetica", 14), command=Jouer)
jouer_button.pack(pady=10)


# le buton de loop n'est pas prêt
# loop_button = Button(root, text="Jouer automatiquement", font=("Helvetica", 14), command=Jouer_loop)
# loop_button.pack(pady=10)


init()
root.mainloop()