from tkinter import *
import random
from PIL import Image, ImageTk



root = Tk()
root.title('Nsi Project 3')
photo = PhotoImage(file = "images/icon.png")
root.iconphoto(False, photo)

root.geometry("900x500")
root.configure(background="#F5F1ED")

# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((150, 218))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Shuffle The Cards
def shuffle():
	# Define Our Deck
	suits = ["diamonds", "clubs", "hearts", "spades"]
	values = range(2, 15)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

	global deck
	deck =[]

	for suit in suits:
		for value in values:
			deck.append(f'{value}_of_{suit}')

	# Create our players
	global player1 , player2
	player1  = []
	player2 = []

	# Grab a random Card For player 1 
	card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(card)
	# Append Card To player 1  List
	player1.append(card)
	# Output Card To Screen
	global player1_image
	player1_image = resize_cards(f'images\card_test.jpg')
	player1_label.config(image=player1_image)

	# Grab a random Card For Player
	card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(card)
	# Append Card To player 1  List
	player2.append(card)
	# Output Card To Screen
	global player2_image
	player2_image = resize_cards(f'images\card_test.jpg')
	player2_label.config(image=player2_image)

	# Put number of remaining cards in title bar
	root.title(f'Nsi Project 3 - {len(deck)} Cards Left')


# Deal Out Cards
def deal_cards():
	try:
		# Get the player1 Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To player 1  List
		player1.append(card)
		# Output Card To Screen
		global player1_image
		player1_image = resize_cards(f'images\card_test.jpg')
		player1_label.config(image=player1_image)

		# Get the player2 Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To player 1  List
		player2.append(card)
		# Output Card To Screen
		global player2_image
		player2_image = resize_cards(f'images\card_test.jpg')
		player2_label.config(image=player2_image)

		# Put number of remaining cards in title bar
		root.title(f'Nsi Project 3 - {len(deck)} Cards Left')

	except:
		root.title(f'Nsi Project 3 - No Cards In Deck')
		print("no more cards")




my_frame = Frame(root, bg="#F5F1ED")
my_frame.pack(pady=20)

# Create Frames For Cards
player1_frame = LabelFrame(my_frame, text="Player 1" , fg='white', bd=0, bg="#252323")
player1_frame.grid(row=0, column=0, padx=20, ipadx=30)

player2_frame = LabelFrame(my_frame, text="Player 2" , fg='white', bd=0, bg="#252323")
player2_frame.grid(row=0, column=1, ipadx=30)

# Put cards in frames
player1_label = Label(player1_frame, text='')
player1_label.pack(pady=20)

player2_label = Label(player2_frame, text='')
player2_label.pack(pady=20)


# Create a couple buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command=deal_cards)
card_button.pack(pady=20)



# Shuffle Deck On Start
shuffle()


root.mainloop()