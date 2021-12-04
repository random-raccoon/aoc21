with open("day01/input.txt", "r") as f:
    count = 0
    firstNum = True
    lastNum = 0
    values = [int(line) for line in f]
    total = values[0] + values[1] + values[2]
    for i in range(0, len(values) - 3):
        newTotal = total - values[i] + values[i+3]
        if newTotal > total:
            count += 1
        total = newTotal

    print(count)