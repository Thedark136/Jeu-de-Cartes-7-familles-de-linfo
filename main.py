#     _   _______ ____   _____
#    / | / / ___//  _/  |__  /
#   /  |/ /\__ \ / /     /_ < 
#  / /|  /___/ // /    ___/ / 
# /_/ |_//____/___/   /____/  

# on importe les librairies pour l'interface graphique et le jeu
from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title('Nsi Project 3')
#l'aspect ratio de la fenetre
root.geometry("1000x550")
#la image de la background

bg = PhotoImage(file="images/icon.png")
# Create Canvas
canvas = Canvas(root, width = 1000, height = 550)
canvas.pack(fill = "both", expand = True)
# Display image
canvas.create_image( 0, 0, image = bg, anchor = "nw")

# on donne une icon au UI 
photo = PhotoImage(file = "images/icon.png")
root.iconphoto(False, photo)
root.resizable(0,0)

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



# fonction qui prend toutes les cartes et les rangent dans une liste
def cards(cartes):
    mes_cartes = []
    for elt in cartes:
        for j in range(len(cartes[elt])):
            mes_cartes.append(cartes[elt][j])
    return mes_cartes

#fonction qui melange les cartes et renvoie une liste contenant les tuples des cartes melanges
def mélanger(cartes):
    mes_cartes = cards(cartes)
    random.shuffle(mes_cartes)
    return mes_cartes

# fonction pour initialiser la photo du derriere des cartes au debut du programme
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


# fonction pour commence le jeux
def commencer1():
    # on melange le cartes pour les preparer a diffuser aux 2 joueurs
    cartes = mélanger(les_cartes)
    global joueur_1
    global joueur_2
    joueur_1 = []
    joueur_2 = []
    #une loop pour distribuer les cartes melangees
    for i in range (0,len(cartes),2):
        joueur_1.append(cartes[i])
        joueur_2.append(cartes[i+1])
    #changer le boutton pour rejouer
    commence_button.config(text="Rejouer")
    joueur1_frame.config(text=f"Joueur 1 - Cartes :  {len(joueur_1)}")
    joueur2_frame.config(text=f"Joueur 2 - Cartes :  {len(joueur_2)}")

def commencer2():
    # on melange le cartes pour les preparer a diffuser aux 2 joueurs
    cartes = mélanger(les_cartes)
    global joueur_1
    global joueur_2
    joueur_1 = []
    joueur_2 = []
    #une loop pour distribuer les cartes melangees
    for i in range (0,len(cartes),2):
        joueur_1.append(cartes[i])
        joueur_2.append(cartes[i+1])
    #changer le boutton pour rejouer
    commence_button.config(text="Rejouer")
    update_listbox(joueur_1, joueur_2)
    joueur1_frame.config(text=f"Joueur 1 - Cartes :  {len(joueur_1)}")
    joueur2_frame.config(text=f"Joueur 2 - Cartes :  {len(joueur_2)}")

def Jouer1():
    #initialisation des nombres de victoire
    joueur_1_victoire = 0
    joueur_2_victoire = 0
    #on change le titre de la fenetre pour dire le nombre de victoire
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
    
    #on compare les cartes et donne les 2 cartes au gagnant
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
    
    #on affiche le nombre de cartes
    joueur1_frame.config(text=f"Joueur 1 - Cartes :  {len(joueur_1)}")
    joueur2_frame.config(text=f"Joueur 2 - Cartes :  {len(joueur_2)}")
    
    # on affiche les prochaines images au joueur
    global joueur1_image
    joueur1_image = resize_cards(f'Cartes/{joueur_1[0][0]}.png')
    joueur1_label.config(image=joueur1_image)
    
    global joueur2_image
    joueur2_image = resize_cards(f'Cartes/{joueur_2[0][0]}.png')
    joueur2_label.config(image=joueur2_image)
    

def update_listbox(joueur_1, joueur_2):
    joueur_1_listbox.delete(0, END)
    for i in range(len(joueur_1)):
        joueur_1_listbox.insert(i, joueur_1[i][0])

    joueur_2_listbox.delete(0, END)
    for i in range(len(joueur_2)):
        joueur_2_listbox.insert(i, joueur_2[i][0])

# cette partie du code est toujours en developement
def Jouer2():
    #initialisation des nombres de victoire
    joueur_1_victoire = 0
    joueur_2_victoire = 0
    #on change le titre de la fenetre pour dire le nombre de victoire
    root.title(f'Projet NSI 3 - Victoires du Joueur 1 : {joueur_1_victoire}, Victoires du Joueur 2: {joueur_1_victoire}')
    
    update_listbox(joueur_1, joueur_2)
    
	# on voit qui gagne 
    if len(joueur_1)==0:
        joueur_2_victoire+=1
        root.title(f'Projet NSI 3 - Victoires du Joueur 1 : {joueur_1_victoire}, Victoires du Joueur 2: {joueur_1_victoire}')
        return ("Joueur 2 a gagné le match")

    elif len(joueur_2)==0:
        joueur_1_victoire+=1
        root.title(f'Projet NSI 3 - Victoires du Joueur 1 : {joueur_1_victoire}, Victoires du Joueur 2: {joueur_1_victoire}')
        return("Joueur 1 a gagné le match")

    #on compare les cartes et donne les 2 cartes au gagnant
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
        
    update_listbox(joueur_1, joueur_2)
    #on affiche le nombre de cartes
    joueur1_frame.config(text=f"Joueur 1 - Cartes :  {len(joueur_1)}")
    joueur2_frame.config(text=f"Joueur 2 - Cartes :  {len(joueur_2)}")


def choisir1():

    carte_1 = joueur_1_listbox.get(ANCHOR)
    
    for i in range(len(joueur_1)):
        if joueur_1[i][0]==carte_1:
            carte_1 = joueur_1[i]
            indice = i
    del joueur_1[i]
    joueur_1.insert(0, carte_1)
    print(joueur_1[0])
    
    global joueur1_image
    joueur1_image = resize_cards(f'Cartes/{carte_1[0]}.png')
    joueur1_label.config(image=joueur1_image)
    
def choisir2():
    carte_2 = joueur_2_listbox.get(ANCHOR)
    
    for i in range(len(joueur_2)):
        if joueur_2[i][0]==carte_2:
            carte_2 = joueur_2[i]
            indice = i
    del joueur_2[i]
    joueur_2.insert(0, carte_2)
    print(joueur_2[0])
    
    global joueur2_image
    joueur2_image = resize_cards(f'Cartes/{carte_2[0]}.png')
    joueur2_label.config(image=joueur2_image)


def vers1():
    global commence_button
    vers1_button.destroy()
    vers2_button.destroy()
    # Créer un bouton pour démarrer le jeu et jouer aux cartes
    jouer_button = Button(canvas, text="Jouer", font=("Helvetica", 14), command=Jouer1)
    jouer_button.pack(pady=10)
    commence_button = Button(canvas, text="Commencer", font=("Helvetica", 14), command=commencer1)
    commence_button.pack(pady=10)


def vers2():
    global commence_button
    global joueur_1_listbox
    global joueur_2_listbox
    vers1_button.destroy()
    vers2_button.destroy()
    # Créer un bouton pour démarrer le jeu et jouer aux cartes
    jouer_button = Button(canvas, text="Jouer", font=("Helvetica", 14), command=Jouer2)
    jouer_button.pack(pady=10)
    commence_button = Button(canvas, text="Commencer", font=("Helvetica", 14), command=commencer2)
    commence_button.pack(pady=10)

    
    joueur_1_listbox = Listbox(my_frame)
    joueur_2_listbox = Listbox(my_frame)
    joueur_1_listbox.grid(row=0, column=0, padx=15)
    joueur_2_listbox.grid(row=0, column=3, padx= 15)
    

    choisir_1_button = Button(my_frame, text="Choisir",font=("Helvetica", 14), command=choisir1)
    choisir_2_button = Button(my_frame, text="Choisir",font=("Helvetica", 14), command=choisir2)
    
    choisir_1_button.grid(row=1, column=0, pady= 10)
    choisir_2_button.grid(row=1, column=3, pady= 10)

#on travail toujours sur une fonction pour automatiser le jeu mais il
# y a des problemes avec l'affichage des images

#dangerzone: ce code crash le programe !ne pas utiliser!
# def Jouer_loop():
#     while joueur_1 != 0 and joueur_2 != 0:
#         Jouer()
#         time.sleep(0.001)
#dangerzone

my_frame = Frame(canvas, background="grey")
my_frame.pack(pady=20)

# Créer des cadres pour les cartes
joueur1_frame = LabelFrame(my_frame, text="Player 1" , fg='white', bd=0, bg="grey")
joueur1_frame.grid(row=0, column=1, padx=20, ipadx=0, pady= 10)

joueur2_frame = LabelFrame(my_frame, text="Player 2" , fg='white', bd=0, bg="grey")
joueur2_frame.grid(row=0, column=2, padx=20, ipadx=0, pady= 10)

# Mettre les cartes dans des cadres
joueur1_label = Label(joueur1_frame, text='',fg='white')
joueur1_label.pack(pady=20)

joueur2_label = Label(joueur2_frame, text='', fg='white')
joueur2_label.pack(pady=20)


#version buttons
vers1_button = Button(canvas, text="Version auto",font=("Helvetica", 14), command=vers1)
vers2_button = Button(canvas, text="Version control",font=("Helvetica", 14), command=vers2)
vers1_button.pack(pady=10)
vers2_button.pack(pady=10)




# ----------------------------------------------------
# le bouton de loop n'est pas prêt
# loop_button = Button(root, text="Jouer automatiquement", font=("Helvetica", 14), command=Jouer_loop)
# loop_button.pack(pady=10)


init()
root.mainloop()