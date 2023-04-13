# libraries
from tkinter import *
import random
from PIL import Image, ImageTk
# main window
root = Tk()
root.title('Jeu de bataille')
root.geometry('900x550')
# icon image
icon = PhotoImage(file = "images/icon.png")
root.iconphoto(False, icon)
root.resizable(0,0)
# playing space
# titles / splitting up the space + default cards
titles = Frame(root)
titles.columnconfigure(0, weight=1)
titles.columnconfigure(1, weight=1)
titles.columnconfigure(2, weight=1)
titles.columnconfigure(3, weight=1)
player1Title = Label(titles, text="Player 1")
player1Title.grid(row = 0, column = 1)
player2Title = Label(titles, text="Player 2")
player2Title.grid(row = 0, column = 2)
# back images, we use label to grid them
holderLabel1 = Label(titles, text = '.')
holderLabel2 = Label(titles, text = '.')
holderLabel1.grid(row= 1, column= 1)
holderLabel2.grid(row= 1, column= 2)
titles.pack(fill='x', pady=30)
# resizing cards 
def resize_cards(card):
	our_card_img = Image.open(card)
	our_card_resize_image = our_card_img.resize((150, 218))
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)
	return our_card_image
# default cards for the beginning of the game
def init():
    global joueur1_image
    joueur1_image = resize_cards(f'Cartes/back.png')
    holderLabel1.config(image=joueur1_image)
    global joueur2_image
    joueur2_image = resize_cards(f'Cartes/back.png')
    holderLabel2.config(image=joueur2_image)
# handing out decks 
# note to self - figure out how to distribute Turing later on 
def distributeDeck() :
    global firstDeck
    global secondDeck
    random.shuffle(listCards)
    firstDeck = [listCards[i] for i in range (22)]
    secondDeck = [listCards[i] for i in range (22, 44)]
    return ([firstDeck, secondDeck])
# versions of the game
def controlLayout():
    global cardCounter1
    global cardCounter2
    global joueur_1_listbox
    global joueur_2_listbox
    autovButton.destroy()
    ctrlvButton.destroy()
    distributeDeck()
    joueur_1_listbox = Listbox(titles, width=30)
    joueur_2_listbox = Listbox(titles, width=30)
    for i in range (len(firstDeck)) :
        joueur_1_listbox.insert(END, firstDeck[i])
        joueur_2_listbox.insert(END, secondDeck[i])
    joueur_1_listbox.grid(row= 1, column= 0)
    joueur_2_listbox.grid(row= 1, column= 4, padx= 30)
    # putting the 2 choice buttons and the play button
    choisir_1_button = Button(titles, text="Choisir",font=("Helvetica", 14), command=choisir1)
    choisir_2_button = Button(titles, text="Choisir",font=("Helvetica", 14), command=choisir2)
    choisir_1_button.grid(row=2, column=0, pady= 10)
    choisir_2_button.grid(row=2, column=3, pady= 10)
    playButton = Button(root, text="Play", font="Helvetica, 14", width=30, command=Jouer2)
    playButton.pack(pady=10)
    cardCounter1 = Label(titles, text=f"Nombre de cartes : {len(firstDeck)}")
    cardCounter2 = Label(titles, text=f"Nombre de cartes : {len(secondDeck)}")
    cardCounter1.grid(row = 2, column = 1)
    cardCounter2.grid(row = 2, column = 2)
    titles.pack(fill="x")
def autoVersion():
    global commence_button
    ctrlvButton.destroy()
    autovButton.destroy()
    # Créer un bouton pour démarrer le jeu et jouer aux cartes
    jouer_button = Button(root, text="Jouer", font=("Helvetica", 14) )
    jouer_button.pack(pady=10)
    commence_button = Button(root, text="Commencer", font=("Helvetica", 14))
    commence_button.pack(pady=10)
# functions to choose cards
def choisir1():
    carte_1 = joueur_1_listbox.get(ANCHOR)
    for i in range(len(firstDeck)):
        if firstDeck[i][0]==carte_1:
            carte_1 = firstDeck[i]
            indice = i
    del firstDeck[i]
    firstDeck.insert(0, carte_1)    
    global joueur1_image
    joueur1_image = resize_cards(f'Cartes/{carte_1[0]}.png')
    holderLabel1.config(image=joueur1_image)
def choisir2():
    carte_2 = joueur_2_listbox.get(ANCHOR)
    for i in range(len(secondDeck)):
        if secondDeck[i][0]==carte_2:
            carte_2 = secondDeck[i]
            indice = i
    del secondDeck[i]
    secondDeck.insert(0, carte_2)
    global joueur2_image
    joueur2_image = resize_cards(f'Cartes/{carte_2[0]}.png')
    holderLabel2.config(image=joueur2_image)
# functions to define the game's mechanics
# update function
def update_listbox():
    joueur_1_listbox.delete(0, END)
    for i in range(len(firstDeck)):
        joueur_1_listbox.insert(i, firstDeck[i][0])
    joueur_2_listbox.delete(0, END)
    for i in range(len(secondDeck)):
        joueur_2_listbox.insert(i, secondDeck[i][0])
# jouer2 is activated once we hit the "play button"
def Jouer2():
    #initialisation des nombres de victoire
    joueur_1_victoire = 0
    joueur_2_victoire = 0
    #on change le titre de la fenetre pour dire le nombre de victoire
    root.title(f'Projet NSI 3 - Victoires du Joueur 1 : {joueur_1_victoire}, Victoires du Joueur 2: {joueur_1_victoire}')
    
    update_listbox()
    
	# on voit qui gagne 
    if len(firstDeck)==0:
        joueur_2_victoire+=1
        root.title(f'Projet NSI 3 - Victoires du Joueur 1 : {joueur_1_victoire}, Victoires du Joueur 2: {joueur_1_victoire}')
        return ("Joueur 2 a gagné le match")
    elif len(secondDeck)==0:
        joueur_1_victoire+=1
        root.title(f'Projet NSI 3 - Victoires du Joueur 1 : {joueur_1_victoire}, Victoires du Joueur 2: {joueur_1_victoire}')
        return("Joueur 1 a gagné le match")

    #on compare les cartes et donne les 2 cartes au gagnant
    # sauf si c'est une egalite
    if firstDeck[0][1]>secondDeck[0][1]:
        print("Joueur 1 gagne la manche")
        firstDeck.append(secondDeck[0])
        firstDeck.append(firstDeck.pop(0))
        secondDeck.remove(secondDeck[0])
    
    elif secondDeck[0][1]>firstDeck[0][1]:
        print("Joueur 2 gagne la manche")
        secondDeck.append(firstDeck[0])
        secondDeck.append(secondDeck.pop(0))
        secondDeck.remove(secondDeck[0])
    else:
        print("égalité")
        firstDeck.append(firstDeck.pop(0))
        secondDeck.append(secondDeck.pop(0))
        
    update_listbox()
    #on affiche le nombre de cartes
    cardCounter1.config(text=f"Joueur 1 - Cartes :  {len(firstDeck)}")
    cardCounter2.config(text=f"Joueur 2 - Cartes :  {len(secondDeck)}")

# function buttons 
ctrlvButton = Button(root, text="Play with a friend", font = ("Helvetica", 12), width= 30, command=controlLayout)
autovButton = Button(root, text="Simulate a game automatically", font= ("Helvetica", 12), width= 30, command=autoVersion)
ctrlvButton.pack(pady= 30)
autovButton.pack(pady= 0)
# dictionnary and list of cards, dictionnary will be used for the 2nd game and list for the 1st as it's more practical
dictionnaryCards = {
    "Sécurité et confidentialité":[("Jules César",1),("AL-Kindi",2),("Diffie Hellman",3),("Rivest-Shamir-Adleman (RSA)",4),("Shafi Goldwasser",5),("Cynthia Dwork",6)],
    "Algorithmes & Programmation":[("Al-Khwarizmi",1), ("Ada Lovelace",2), ("Grace Hopper",3), ("Dorothy Vaughan",4), ("Gilles Kahn",5), ("Gérard Berry",6)],
    "Mathématiques & Informatique":[("Hypatie d'Alexandrie",1), ("George Boole",2), ("Alonzo Church",3), ("Jacques-Louis Lions",4), ("Ingrid Daubechies",5), ("Jocelyne Troccaz",6)],
    "Intelligence Artificielle":[("Herbert Simon",1), ("Marvin Minsky",2), ("Geoffrey Hinton",3), ("Rose Dieng-Kuntz",4), ("Yann LeCun",5), ("Cordelia Schmid",6)],
    "Machines & Composants":[("Charles Babbage",1), ("John von Neumann",2), ("Hedy Lamarr",3), ("Seymour Cray",4), ("Gordon Moore",5), ("Hiroshi Ishiguro",6)],
    "Interaction Homme-Machine":[("Doug Engelbart",1), ("Ted Nelson",2), ("Alan Kay",3), ("Joëlle Coutaz",4), ("Jean-Marie Hullot",5), ("Marie-Paule Cani",6)],
    "Systèmes & réseaux":[("Alexander Graham Bell",1), ("Claude Shannon",2), ("Vinton Cerf",3), ("Tim Berners-Lee",4), ("Pascale Vicat-Blanc",5), ("Anne-Marie Kermarrec",6)],
    "Joker":[("Alan Turing",7),("Alan Turing",7)]
}
listCards = [
    ("Jules César",1),("AL-Kindi",2),("Diffie Hellman",3),("Rivest-Shamir-Adleman (RSA)",4),
    ("Shafi Goldwasser",5),("Cynthia Dwork",6),("Al-Khwarizmi",1), ("Ada Lovelace",2), ("Grace Hopper",3),
    ("Dorothy Vaughan",4), ("Gilles Kahn",5), ("Gérard Berry",6),("Hypatie d'Alexandrie",1), ("George Boole",2),
    ("Alonzo Church",3), ("Jacques-Louis Lions",4), ("Ingrid Daubechies",5), ("Jocelyne Troccaz",6),
    ("Herbert Simon",1), ("Marvin Minsky",2), ("Geoffrey Hinton",3), ("Rose Dieng-Kuntz",4), ("Yann LeCun",5),
    ("Cordelia Schmid",6), ("Charles Babbage",1), ("John von Neumann",2), ("Hedy Lamarr",3),
    ("Seymour Cray",4), ("Gordon Moore",5), ("Hiroshi Ishiguro",6),("Doug Engelbart",1), ("Ted Nelson",2),
    ("Alan Kay",3), ("Joëlle Coutaz",4), ("Jean-Marie Hullot",5), ("Marie-Paule Cani",6),
    ("Alexander Graham Bell",1),("Claude Shannon",2), ("Vinton Cerf",3), ("Tim Berners-Lee",4), 
    ("Pascale Vicat-Blanc",5), ("Anne-Marie Kermarrec",6),("Alan Turing",7),("Alan Turing",7)]
init()
root.mainloop()