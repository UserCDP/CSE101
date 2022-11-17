import random

class Card:
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f'{self.rank_names[self.rank]} of {self.suit_names[self.suit]}'

	def __eq__(self, other):
		return self.rank == other.rank and self.suit == other.suit

	def __gt__(self, other):
		if self.rank > other.rank:
			return True
		if self.rank == other.rank:
			if self.suit > other.suit:
				return True
		return False

class Deck:
	def __init__(self, minrank):
		self.cards = []
		rank_names = Card.rank_names
		suit_names = Card.suit_names
		for suit in suit_names:
			for rank in rank_names:
				if minrank <= rank_names.index(rank):
					self.cards.append(Card(suit_names.index(suit), rank_names.index(rank)))

	def __str__(self):
		l = []
		for card in self.cards:
			l.append(str(card))
		return ', '.join(l) 

	def pop(self):
		last_card = self.cards[len(self.cards)-1]
		self.cards.remove(last_card)
		return last_card

	def shuffle(self):
		random.shuffle(self.cards)
		
class Player:
	def __init__(self, name):
		self.name = name
		self.hand = Deck(13)

	def __str__(self):
		return f'Player {self.name} {"has no cards" if len(self.hand.cards) == 0 else "has: " + str(self.hand)}'

	def add_card(self, card):
		self.hand.cards.append(card)

	def num_cards(self):
		return len(self.hand.cards)

	def remove_card(self):
		first_card = self.hand.cards[0]
		self.hand.cards.remove(first_card)
		return first_card


class CardGame:

	def __init__(self, player_names, minrank):
		self.players = []
		for player in player_names:
			self.players.append(Player(player))
		self.deck = Deck(minrank)
		self.numcards = len(self.deck.cards)
	
	def __str__(self):
		st = ''
		for player in self.players:
			st += (str(player)) + '\n'
		return st

	def burn_card(self, card):
		self.deck.cards.remove(card)
