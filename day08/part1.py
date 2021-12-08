def decode(input):
    [patterns, output] = [s.strip().split(' ') for s in input.strip().split('|')]
    # Part 1 is simple; ignore patterns and just count segments in the output.

    count = 0
    for entry in output:
        numSegments = len(entry)
        if numSegments == 2:  # 1
            count += 1
        elif numSegments == 3: # 7
            count += 1
        elif numSegments == 4: # 4
            count += 1
        elif numSegments == 7: # 8
            count += 1
    return count

with open('day08/input.txt', 'r') as f:
    count = 0
    for line in f:
        count += decode(line)
    print(count)
