import re

class Board:
    def __init__(self, line1: str, line2: str, line3: str, line4: str, line5: str):
        self.grid = []
        self.marked = []
        self.addLine(line1)
        self.addLine(line2)
        self.addLine(line3)
        self.addLine(line4)
        self.addLine(line5)

    def addLine(self, line: str):
        self.grid.append([int(n) for n in re.split(' +', line.strip())])
        self.marked.append([False] * len(self.grid[0]))

    def maybeMark(self, number: int):
        for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid[x])):
                if self.grid[x][y] == number:
                    self.marked[x][y] = True
                
    def won(self) -> bool:
        # check rows
        for x in range(0, len(self.marked)):
            allMarked = True
            for y in range(0, len(self.marked[x])):
                allMarked = allMarked and self.marked[x][y]
            if allMarked:
                return True

        # check columns
        for x in range(0, len(self.marked)):
            allMarked = True
            for y in range(0, len(self.marked[x])):
                allMarked = allMarked and self.marked[y][x]
            if allMarked:
                return True

        return False

    def score(self, number: int) -> int:
        sum = 0
        for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid[x])):
                if not self.marked[x][y]:
                    sum += self.grid[x][y]
        return sum * number


with open('day04/input.txt', 'r') as f:
    numbers = [int(n) for n in f.readline().strip().split(',')]

    boards = []

    while f.readline() != '':
        boards.append(Board(f.readline(), f.readline(), f.readline(), f.readline(), f.readline()))

    won = False
    for number in numbers:
        for board in boards:
            board.maybeMark(number)
        if len(boards) == 1 and boards[0].won():
            print(boards[0].score(number))
            break
        boards = [board for board in boards if not board.won()]
