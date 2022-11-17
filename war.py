class Card:
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f'{self.rank_names[self.rank]} of {self.suit_names[self.suit]}'
