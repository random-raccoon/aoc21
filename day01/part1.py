with open("day01/input.txt", "r") as f:
    count = 0
    firstNum = True
    lastNum = 0
    for line in f:
        n = int(line)
        if firstNum:
            firstNum = False
        else:
            if n > lastNum:
                count += 1
        lastNum = n

    print(count)