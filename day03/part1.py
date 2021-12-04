with open('day03/input.txt', 'r') as f:
    data = [line.strip() for line in f]
    counts = [0] * len(data[0])
    for entry in data:
        for i in range(0, len(entry)):
            if (entry[i] == '1'):
                counts[i] += 1

    gamma = 0
    epsilon = 0
    for c in counts:
        gamma *= 2
        epsilon *= 2
        if c > len(data) / 2:
            gamma += 1
        else:
            epsilon += 1

    print(gamma)
    print(epsilon)
    print(gamma * epsilon)