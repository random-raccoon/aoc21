def mostCommonBitValue(entries, bitIndex):
    count = 0
    for entry in entries:
        if entry[bitIndex] == '1':
            count += 1
    if count >= len(entries)/2:
        return '1'
    return '0'

def leastCommonBitValue(entries, bitIndex):
    count = 0
    for entry in entries:
        if entry[bitIndex] == '1':
            count += 1
    if count >= len(entries)/2:
        return '0'
    return '1'

def toInt(s: str):
    v = 0
    for c in s:
        v *= 2
        if c == '1':
            v += 1
    return v

with open('day03/input.txt', 'r') as f:
    data = [line.strip() for line in f]

    o2rating = data
    co2rating = data
    
    index = 0
    while len(o2rating) > 1:
        bit = mostCommonBitValue(o2rating, index)
        o2rating = list(filter(lambda entry: entry[index] == bit, o2rating))
        index += 1

    index = 0
    while len(co2rating) > 1:
        bit = leastCommonBitValue(co2rating, index)
        co2rating = list(filter(lambda entry: entry[index] == bit, co2rating))
        index += 1

    print(toInt(o2rating[0]) * toInt(co2rating[0]))