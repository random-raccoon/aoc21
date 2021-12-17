from heapq import heappush, heappop

# heap that holds (step_cost, x, y)
points = []

# set of points that will be visited or already have been.
# These points will not be enqueued again.  Safe, because the 
# anticipated cost will not decrease on a second visit.
queued_points = set()

def add_neighbours(x, y):
    cost = costs[x][y]

    if x > 0 and (x-1, y) not in queued_points:
        queued_points.add((x-1, y))
        heappush(points, (cost + map[x-1][y], x-1, y))

    if x < width-1 and (x+1, y) not in queued_points:
        queued_points.add((x+1, y))
        heappush(points, (cost + map[x+1][y], x+1, y))

    if y > 0 and (x, y-1) not in queued_points:
        queued_points.add((x, y-1))
        heappush(points, (cost + map[x][y-1], x, y-1))

    if y < height-1 and (x, y+1) not in queued_points:
        queued_points.add((x, y+1))
        heappush(points, (cost + map[x][y+1], x, y+1))


def find_cost(x, y):
    contenders = []
    if x > 0 and costs[x-1][y] != None:
        contenders.append(costs[x-1][y])

    if x < width-1 and costs[x+1][y] != None:
        contenders.append(costs[x+1][y])

    if y > 0 and costs[x][y-1] != None:
        contenders.append(costs[x][y-1])

    if y < height-1 and costs[x][y+1] != None:
        contenders.append(costs[x][y+1])

    return min(contenders)


map = []
with open('day15/input.txt', 'r') as f:
    for line in f:
        map.append([int(c) for c in line.strip()])

width = len(map)
height = len(map[0])

# Bigify the map.  This is gross, but just one line...
big_map = [[(map[x%width][y%height] + x // width + y // height - 1) % 9 + 1 for y in range(height * 5)] for x in range(width * 5)]
map = big_map
width = len(map)
height = len(map[0])

costs = [[None for y in range(height)] for x in range(width)]

x, y = width-1, height-1 
costs[x][y] = map[x][y]
add_neighbours(x, y)
while True:
    (_, x, y) = heappop(points)
    cost = find_cost(x, y)
    if x == 0 and y == 0:
        # Made it!
        print(cost)
        break

    costs[x][y] = cost + map[x][y]
    add_neighbours(x, y)
