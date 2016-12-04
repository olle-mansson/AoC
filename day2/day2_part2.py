class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


file = open('input.txt')
code = []
allowed_positions = {Position(0, 2): 1, Position(-1, 1): 2, Position(0, 1): 3,
                     Position(1, 1): 4, Position(-2, 0): 5, Position(-1, 0): 6,
                     Position(0, 0): 7, Position(1, 0): 8, Position(2, 0): 9,
                     Position(-1, -1): 'A', Position(0, -1): 'B',
                     Position(1, -1): 'C', Position(0, -2): 'D'}
current_pos = Position(-2, 0)

for line in file:
    for order in line:
        if order == 'U' and (current_pos + Position(0, 1)) in allowed_positions:
            current_pos = current_pos + Position(0, 1)
        elif order == 'D' and (current_pos + Position(0, -1)) in allowed_positions:
            current_pos = current_pos + Position(0, -1)
        elif order == 'L' and (current_pos + Position(-1, 0)) in allowed_positions:
            current_pos = current_pos + Position(-1, 0)
        elif order == 'R' and (current_pos + Position(1, 0)) in allowed_positions:
            current_pos = current_pos + Position(1, 0)
    code.append(allowed_positions[current_pos])

print(code)
