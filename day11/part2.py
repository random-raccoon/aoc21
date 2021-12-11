class World:
    def __init__(self, data):
        self.data = data
        self.width = len(data)
        self.height = len(data[0])
        self.allFlashed = False

    def step(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.data[x][y] += 1
                if self.data[x][y] == 10:
                    self.flash(x, y)

        # Reset flashed cells and check flashes.
        self.allFlashed = True
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.data[x][y] > 9:
                    self.data[x][y] = 0
                else:
                    self.allFlashed = False
        

    def flash(self, x: int, y: int):
        for dx in range(-1, 2):
            tx = x + dx
            if tx >= 0 and tx < self.width:
                for dy in range(-1, 2):
                    ty = y + dy
                    if ty >= 0 and ty < self.height:
                        self.data[tx][ty] += 1
                        if self.data[tx][ty] == 10:
                            self.flash(tx, ty)

    def __repr__(self):
        return '\n'.join([''.join(str(i) for i in row) for row in self.data])

with open('day11/input.txt', 'r') as f:
    data = []
    for line in f:
        data.append([int(c) for c in line.strip()])
    
    world = World(data)

    step = 0
    while not world.allFlashed:
        world.step()
        step += 1
    
    print(step)