import re

class Point:
    def __init__(self, text: str):
        [self.x, self.y] = [int(v) for v in text.split(',')]

    def __repr__(self):
        return f'({self.x},{self.y})'

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def isHorizontal(self):
        return self.p1.y == self.p2.y

    def isVertical(self):
        return self.p1.x == self.p2.x

    def __repr__(self):
        return f'{self.p1} -> {self.p2}'

    def __iter__(self):
        return LineIterator(self)

class LineIterator:
    def __init__(self, line: Line):
        self.length = 0
        self.x = line.p1.x
        self.y = line.p1.y
        self.dx = 0
        if line.p1.x != line.p2.x:
            self.dx = (line.p2.x - line.p1.x) // abs(line.p2.x - line.p1.x)
            self.length = abs(line.p2.x - line.p1.x) + 1
        self.dy = 0
        if line.p1.y != line.p2.y:
            self.dy = (line.p2.y - line.p1.y) // abs(line.p2.y - line.p1.y)
            self.length = abs(line.p2.y - line.p1.y) + 1
        self.index = 0

    def __next__(self) -> list[int]:
        if (self.index < self.length):
            x = self.x + self.index * self.dx
            y = self.y + self.index * self.dy
            self.index += 1
            return [x,y]
        raise StopIteration

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.data = [0] * width * height

    def addLine(self, line: Line):
        for [x, y] in line:
            self.data[x + y * self.width] += 1

    def countOverlaps(self) -> int:
        count = 0
        for p in self.data:
            if p > 1:
                count += 1
        return count

with open('day05/input.txt', 'r') as f:

    lines = []
    maxX = 0
    maxY = 0

    for textLine in f:
        points = re.split(' -> ', textLine.strip())
        line = Line(Point(points[0]), Point(points[1]))
        lines.append(line)
        maxX = max(maxX, line.p1.x, line.p2.x)
        maxY = max(maxY, line.p1.y, line.p2.y)

    grid = Grid(maxX+1, maxY+1)
    for line in lines:
        grid.addLine(line)

    print(grid.countOverlaps())