"""
Copyright Daniela Cojocaru 2022:)
"""
# Exercise 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __hash__(self):
        return hash(str(self))

    def get_neighbors(self):
        return {Point(self.x - 1, self.y - 1),
                Point(self.x - 1, self.y),
                Point(self.x - 1, self.y + 1),
                Point(self.x, self.y - 1),
                Point(self.x, self.y + 1),
                Point(self.x + 1, self.y - 1),
                Point(self.x + 1, self.y),
                Point(self.x + 1, self.y + 1)}

class Board:
    def __init__(self, x_size, y_size, points):
        self.alive_points = points
        self.x_size = x_size
        self.y_size = y_size

    def is_legal(self, point):
        if point.x < 0 or point.y < 0 or point.x > (self.x_size -1) or point.y > (self.y_size - 1):
            return False
        return True

# Exercise 4
    def number_live_neighbors(self, p):
        neighbors = p.get_neighbors()
        alive = 0
        for point in self.alive_points:
            if point in neighbors:
                alive += 1
        return alive

# Exercise 5
    def next_step(self):
        new_alive = set()
        for i in range (0, self.x_size):
            for j in range (0, self.y_size):
                alive_n = self.number_live_neighbors(Point(i,j))
                if Point(i,j) in self.alive_points:
                    if alive_n == 2 or alive_n == 3:
                        new_alive.add(Point(i,j))
                else:
                    if alive_n == 3:
                        new_alive.add(Point(i,j))
        self.alive_points = new_alive

# Exercise 7
    def toggle_point(self, x, y):
        if Point(x,y) in self.alive_points:
            self.alive_points.discard (Point(x,y))
        else:
            self.alive_points.add(Point(x,y))

# Exercise 6
def load_from_file(filename):
    infile = open(filename, 'r')
    points = set()
    k = 0
    for line in infile:
        if k == 2 and len(line) != 0:
            points.add(Point(int(line.split(',')[0]), int(line.split(',')[1])))

        if k == 1:
            y_size = int(line)
            k += 1

        if k == 0:
            x_size = int(line)
            k += 1
    return Board (x_size, y_size, points)

# Exercise 8
def is_periodic(board):
    