class Direction:
    def __init__(self, line):
        parts = line.partition(' ')
        self.command = parts[0]
        self.distance = int(parts[2])

class Position:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def move(self, direction):
        if (direction.command == 'forward'):
            self.horizontal += direction.distance
        elif (direction.command == 'down'):
            self.depth += direction.distance
        elif (direction.command == 'up'):
            self.depth -= direction.distance

with open('day02/input.txt', 'r') as f:
    directions = [Direction(line) for line in f]
    position = Position()
    for direction in directions:
        position.move(direction)

    print(position.horizontal * position.depth)