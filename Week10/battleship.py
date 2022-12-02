"""
Copyright Daniela Cojocaru 2022 - all rights reserved for
uncommented code that shall not make sense later
"""

import random

ship_types = [('Battleship',4),('Carrier',5),('Cruiser',3),('Destroyer',2),('Submarine',3)]

# Exercise 1
class Ship:
	def __init__(self, name, positions):
		self.name = name
		self.positions = positions
		self.hits = set()
		
	def __repr__(self):
		return f"Ship('{self.name}', {self.positions})"
		
	def __str__(self):
		return f'{repr(self)} with hits {self.hits}'
	
	def __eq__(self, other):
		if self.name == other.name:
			if self.positions == other.positions:
				if self.hits == other.hits:
					return True
		return False

	# Exercise 4
	def take_shot(self, shot):
		if shot in self.positions:
			if shot not in self.hits:
				self.hits.add(shot)
				if self.hits == self.positions and len(self.hits) != 0:
					return "DESTROYED"
				elif len(self.hits) == 0:
					return "MISS"
				else:
					return "HIT"
		return "MISS"

		
	def is_afloat(self):
		for position in self.positions:
			if position not in self.hits:
				return True
		return False
		
# Exercise 2
class Grid:
	def __init__(self, x_size, y_size):
		self.x_size = x_size
		self.y_size = y_size
		self.ships = []
		self.misses = set()
		
	def add_ship(self, ship):
		ok = True
		for ship_g in self.ships:
			common = ship_g.positions & ship.positions
			if len(common) != 0:
				ok = False
		if ok:
			self.ships.append(ship)
		
	def shoot(self, position):
		for ship in self.ships:
			status = ship.take_shot(position)
			if status == "HIT":
				return ('HIT', None)
			if status == "DESTROYED":
				return ('DESTROYED', ship)
	
		self.misses.add(position)
		return ('MISS', None)

	# Exercise 7
	def random_ship(self):
		initial_x = random.randint(0, self.x_size)
		initial_y = random.randint(0, self.y_size)
		ship = random.choice(ship_types)
		positions = {(initial_x, initial_y)}

		on_x = random.choice([True, False])
		for k in range(ship[1]):
			if on_x:
				positions.add((initial_x, initial_y+k))
			else:
				positions.add((initial_x + k, initial_y))

		self.add_ship(Ship(ship[0], positions))

	def create_random(self, n):
		while len(self.ships) < n:
				self.random_ship()


# Exercise 6
class BlindGrid:
	def __init__(self, grid):
		self.x_size = grid.x_size
		self.y_size = grid.y_size
		self.misses = grid.misses
		self.hits = set()
		self.sunken_ships = []
		for ship in grid.ships:
			if ship.positions == ship.hits:
				self.sunken_ships.append(ship)
			self.hits = self.hits.union(ship.hits)
				

def create_ship_from_line(text):
	data = text.split(' ')
	name = data[0]
	positions = set()
	for coords in data[1:]:
		x = int(coords.split(":")[0])
		y = int(coords.split(":")[1])
		positions.add((x,y))

	return Ship(name, positions)

def load_grid_from_file(filename):
	infile = open(filename, 'r')
	first_l = True
	for line in infile:
		if first_l:
			x = int(line.split(":")[0])
			y = int(line.split(":")[1])
			g = Grid(x,y)
			first_l = False
		else:
			g.add_ship(create_ship_from_line(line))

	return g