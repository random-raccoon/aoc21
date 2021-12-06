with open('day06/input.txt', 'r') as f:
    population = [int(v) for v in f.read().strip().split(',')]
    buckets = [0] * 9

    # Initialize
    for p in population:
        buckets[p] += 1

    for i in range(0, 256):
        newBuckets = [0] * 9
        newBuckets[8] = buckets[0]
        newBuckets[6] = buckets[0]
        for age in range(1, 9):
            newBuckets[age-1] += buckets[age]
        buckets = newBuckets

    count = 0
    for c in buckets:
        count += c

    print(count)
