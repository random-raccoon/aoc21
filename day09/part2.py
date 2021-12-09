# Note: it is implied that 9's are walls, but I'd rather not make that assumption.

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

def findBasin(r: int, c: int, heightData:list[list[int]], basinData:list[list[int]]) -> int:
    height = heightData[r][c]
    if r > 0 and heightData[r-1][c] < height:
        return basinData[r-1][c]
    if c > 0 and heightData[r][c-1] < height:
        return basinData[r][c-1]
    if r < len(heightData)-1 and heightData[r+1][c] < height:
        return basinData[r+1][c]
    if c < len(heightData[r])-1 and heightData[r][c+1] < height:
        return basinData[r][c+1]
    # This should never happen.

with open('day09/input.txt', 'r') as f:
    heightData = []
    basinData = []
    for line in f:
        heightData.append([int(c) for c in line.strip()])
        basinData.append([0] * len(heightData[0]))

    basinId = 1
    for r in range(0,len(heightData)):
        for c in range(0,len(heightData[r])):
            if (isLowPoint(r, c, heightData)):
                basinData[r][c] = basinId
                basinId += 1

    basinSizes = [1] * (basinId)
    for height in range(1, 9):
        for r in range(0,len(heightData)):
            for c in range(0,len(heightData[r])):
                if heightData[r][c] == height and basinData[r][c] == 0:
                    if (basinId == 0):
                        print(f' oh bother.  Something wrong at {r} {c}')
                    basinId = findBasin(r, c, heightData, basinData)
                    basinData[r][c] = basinId
                    basinSizes[basinId] += 1

    basinSizes.sort(reverse=True)

    print(basinSizes[0] * basinSizes[1] * basinSizes[2])
