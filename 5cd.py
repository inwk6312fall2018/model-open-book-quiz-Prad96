#modeltask-poker
import pyCardDeck #
import itertools, random	#to shuffle 

#class Poker():
def deckgen():			#to generate deck of cards
	suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] #4 suits
	ranks = {'A': 'Ace',
             '2': 'Two',
             '3': 'Three',
             '4': 'Four',
             '5': 'Five',
             '6': 'Six',
             '7': 'Seven',
             '8': 'Eight',
             '9': 'Nine',
             '10': 'Ten',
             'J': 'Jack',
             'Q': 'Queen',
             'K': 'King'}
	cards = []
	for suit in suits:
		for rank, name in ranks.items():
			cards.append(rank)
			cards.append(suit)
			cards.append(name)
	print("Generated deck of cards for the table")
#	print(random.shuffle(cards)) 		#shuffling cards
	print(cards)
deckgen()

	



