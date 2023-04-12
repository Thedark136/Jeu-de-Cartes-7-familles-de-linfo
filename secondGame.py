from tkinter import *
from random import *
from PIL import Image, ImageTk
# base of the root
root = Tk()
root.title('Jeu tro op')
root.attributes('-fullscreen', True)
root.configure(background="#2D2727")
icon = PhotoImage(file = "images/icon.png")
root.iconphoto(False, icon)
root.resizable(0,0)
mainGrid = Frame(root)
mainGrid.configure(background="#2D2727")
username1 = Label(mainGrid, text= "Joueur 1", font=("Helvetica", 16))
username2 = Label(mainGrid, text= "Joueur 2", font=("Helvetica", 16))
# configuring the first grid, 3 columns
mainGrid.columnconfigure(0, weight=1)
mainGrid.columnconfigure(1, weight=1)
mainGrid.columnconfigure(2, weight=1)
username1.grid(row=0, column=0, pady= 20)
username2.grid(row=0, column=2, pady= 20)
mainGrid.pack(fill="x")
# card functions
def resize_cards(card):
	our_card_img = Image.open(card)
	our_card_resize_image = our_card_img.resize((150, 218))
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)
	return our_card_image
def resizeGrid(card):
    our_card_img = Image.open(card)
    our_card_resize_image = our_card_img.resize((80, 133))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    return our_card_image
def init():
    global joueur1_image
    joueur1_image = resize_cards(f'Cartes/back.png')
    holderLabel1.config(image=joueur1_image)
    global joueur2_image
    joueur2_image = resize_cards(f'Cartes/back.png')
    holderLabel2.config(image=joueur2_image)
# function of distribution
def distributeDeck() :
    global firstDeck
    global secondDeck
    global cemetary
    shuffle(listCards)
    firstDeck = [listCards[i] for i in range (10)]
    secondDeck = [listCards[i] for i in range (10, 20)]
    cemetary = [listCards[i] for i in range (20, 40)]
    return ([firstDeck, secondDeck])
# function to start the game, alters the layout
def Start ():
    # globals
    global imageList1
    global imageList2
    startButton.destroy()
    quitButton.grid(row= 8, column= 1)
    # cardGrid layout
    distributeDeck()
    cardGrid1 = Frame(mainGrid)
    cardGrid1.configure(pady=50, background="#2D2727")
    cardGrid1.columnconfigure(0, weight=1)
    cardGrid1.columnconfigure(1, weight=1)
    cardGrid1.columnconfigure(2, weight=1)
    cardGrid1.columnconfigure(3, weight=1)
    cardGrid1.columnconfigure(4, weight=1)
    cardGrid2 = Frame(mainGrid)
    cardGrid2.configure(pady=50, background= "#2D2727")
    cardGrid2.columnconfigure(0, weight=1)
    cardGrid2.columnconfigure(1, weight=1)
    cardGrid2.columnconfigure(2, weight=1)
    cardGrid2.columnconfigure(3, weight=1)
    cardGrid2.columnconfigure(4, weight=1)
    # displays the cards
    gridList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    gridList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    imageList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    imageList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cardCounter1 = 0
    for i in range (2):
        for j in range (5) :
            imageList1[cardCounter1] = resizeGrid(f'Cartes/{firstDeck[cardCounter1][0]}.png')
            gridList1[cardCounter1] = Button(cardGrid1, text= ..., background="#2D2727", borderwidth=0)
            gridList1[cardCounter1].config(image = imageList1[cardCounter1])
            gridList1[cardCounter1].grid(row = i, column = j)
            cardGrid1.grid(row=2, column=0)
            cardCounter1 += 1
    cardCounter2 = 0
    for i in range (2):
        for j in range (5) :
            imageList2[cardCounter2] = resizeGrid(f'Cartes/{secondDeck[cardCounter2][0]}.png')
            gridList2[cardCounter2] = Button(cardGrid2, text= ..., background="#2D2727", borderwidth=0)
            gridList2[cardCounter2].config(image = imageList2[cardCounter2])
            gridList2[cardCounter2].grid(row = i+1, column = j+1)
            cardGrid2.grid(row=2, column=2)                
            cardCounter2 += 1
def Quit():
    root.destroy()
# start up layout
holderLabel1 = Label(mainGrid, text = '.')
holderLabel2 = Label(mainGrid, text = '.')
holderLabel1.grid(row= 1, column= 0)
holderLabel2.grid(row= 1, column= 2)
startButton = Button(mainGrid, text="Commencer", command=Start, width=30, font=("Helvetica", 18), borderwidth=0)
startButton.grid(row= 1, column= 1)
quitButton = Button(mainGrid, text="Sortir", command=Quit, width=30, font=("Helvetica", 18), borderwidth=0)
quitButton.grid(row= 2, column= 1)
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
    ("Pascale Vicat-Blanc",5), ("Anne-Marie Kermarrec",6)]
dictionnaryCards = {
    "Sécurité et confidentialité":[("Jules César",1),("AL-Kindi",2),("Diffie Hellman",3),("Rivest-Shamir-Adleman (RSA)",4),("Shafi Goldwasser",5),("Cynthia Dwork",6)],
    "Algorithmes & Programmation":[("Al-Khwarizmi",1), ("Ada Lovelace",2), ("Grace Hopper",3), ("Dorothy Vaughan",4), ("Gilles Kahn",5), ("Gérard Berry",6)],
    "Mathématiques & Informatique":[("Hypatie d'Alexandrie",1), ("George Boole",2), ("Alonzo Church",3), ("Jacques-Louis Lions",4), ("Ingrid Daubechies",5), ("Jocelyne Troccaz",6)],
    "Intelligence Artificielle":[("Herbert Simon",1), ("Marvin Minsky",2), ("Geoffrey Hinton",3), ("Rose Dieng-Kuntz",4), ("Yann LeCun",5), ("Cordelia Schmid",6)],
    "Machines & Composants":[("Charles Babbage",1), ("John von Neumann",2), ("Hedy Lamarr",3), ("Seymour Cray",4), ("Gordon Moore",5), ("Hiroshi Ishiguro",6)],
    "Interaction Homme-Machine":[("Doug Engelbart",1), ("Ted Nelson",2), ("Alan Kay",3), ("Joëlle Coutaz",4), ("Jean-Marie Hullot",5), ("Marie-Paule Cani",6)],
    "Systèmes & réseaux":[("Alexander Graham Bell",1), ("Claude Shannon",2), ("Vinton Cerf",3), ("Tim Berners-Lee",4), ("Pascale Vicat-Blanc",5), ("Anne-Marie Kermarrec",6)],
}

























    # # TO READ - pour display les cartes jessayi de faire ca bas ma meshe l7al iza bte2daro t7elouwa send help --- im as lost as you are brother
    # for i in listCards : # first deck
    #     for j in firstDeck :
    #         if i == j :
    #             if y <= 4 :
    #                 value = Label(cardGrid1, text='.')
    #                 value.grid(row=x, column=y)
    #                 value.config(image=f'{i[0]}.png')
    #                 y = y + 1 
    #             else :
    #                 y = 0
    #                 x = x + 1
    #                 value = Label(cardGrid1, text='.')
    #                 value.grid(row=x, column=y)
    #                 value.config(image=f'{i[0]}.png')
    # cardGrid1.pack()
    # value = 0
    # x = 0
    # y = 0
    # for i in listCards : # second deck
    #     for j in secondDeck :
    #         if i == j :
    #             if y <= 4 :
    #                 value = Label(cardGrid2, text='.')
    #                 value.grid(row=x, column=y)
    #                 value.config(image=f'{i[0]}.png')
    #                 y = y + 1
    #             else :
    #                 y = 0
    #                 x = x + 1
    #                 value = Label(cardGrid2, text='.')
    #                 value.grid(row=x, column=y)
    #                 value.config(image=f'{i[0]}.png')
    # cardGrid2.pack()

init()
root.mainloop()