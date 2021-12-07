def calcCost(position: int, target: int) -> int:
    n = abs(target - position)
    return (n * (n+1)) // 2

with open('day07/input.txt', 'r') as f:
    positions = [int(p) for p in f.read().strip().split(',')]
    target = 0
    cost = None
    lastCost = None
    while lastCost == None or lastCost >= cost:
        lastCost = cost
        cost = sum([calcCost(p, target) for p in positions])
        target += 1

    print(lastCost)