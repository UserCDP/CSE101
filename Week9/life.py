
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
        new_alive = {}
        for i in range (0, self.x_size):
            for j in range (0, self.y_size):
                if self.number_live_neighbors(Point(i,j)) == 2:
