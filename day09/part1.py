def isLowPoint(r: int, c: int, data:list[list[int]]) -> bool:
    height = data[r][c]
    if r > 0 and data[r-1][c] <= height:
        return False
    if c > 0 and data[r][c-1] <= height:
        return False
    if r < len(data)-1 and data[r+1][c] <= height:
        return False
    if c < len(data[r])-1 and data[r][c+1] <= height:
        return False

    return True

with open('day09/input.txt', 'r') as f:
    data = []
    for line in f:
        data.append([int(c) for c in line.strip()])
    
    value = 0
    for r in range(0,len(data)):
        for c in range(0,len(data[r])):
            if (isLowPoint(r, c, data)):
                value += data[r][c] + 1


    print(value)