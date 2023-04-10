from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title('Nsi Project 3')
#l'aspect ratio de la fenetre
root.geometry("1000x550")
#la image de la background

bg = PhotoImage(file="images/nsi background.png")
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
    "Systèmes & réseaux":[("Alexander Graham Bell",1), ("Claude Shannon",2), ("Vinton Cerf",3), ("Tim Berners-Lee",4), ("Pascale Vi)

joueur_1_label = Label(canvas, text="Joueur 1")
joueur_1_label.pack(padx=10)

root.mainloop()