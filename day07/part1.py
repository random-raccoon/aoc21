with open('day07/input.txt', 'r') as f:
    positions = [int(p) for p in f.read().strip().split(',')]
    # Feeling dumb and can't think of how to directly find the target.  Just search.
    target = 0
    cost = None
    lastCost = None
    while lastCost == None or lastCost >= cost:
        lastCost = cost
        cost = sum([abs(target - p) for p in positions])
        target += 1

    print(lastCost)