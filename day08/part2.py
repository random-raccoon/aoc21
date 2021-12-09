def decode(input):
    [patterns, output] = [[{c for c in w} for w in s.strip().split(' ')] for s in input.strip().split('|')]

    # Find the numbers that we know
    one = [entry for entry in patterns if len(entry) == 2][0]
    seven = [entry for entry in patterns if len(entry) == 3][0]
    four = [entry for entry in patterns if len(entry) == 4][0]
    eight = [entry for entry in patterns if len(entry) == 7][0]
    # Batch together the ones we don't
    len5 = [entry for entry in patterns if len(entry) == 5]
    len6 = [entry for entry in patterns if len(entry) == 6]

    (a,) = seven.difference(one)
    
    nine = [entry for entry in len6 if four.issubset(entry)][0]
    (g,) = nine.difference(four).difference({a})
    (e,) = eight.difference(nine)

    two = [entry for entry in len5 if {a,e,g}.issubset(entry)][0]
    (c,) = one.intersection(two)
    (d,) = two.difference({a,c,e,g})
    (f,) = one.difference({c})

    (b,) = eight.difference({a,c,d,e,f,g})

    # Now that it's fully mapped, fill in the remaining digits.
    three = {a,c,d,f,g}
    five = {a,b,d,f,g}
    six = {a,b,d,e,f,g}

    # Use the digits to calculate the values.
    # Could be more elegant but this works.
    value = 0
    for digit in output:
        value *= 10
        if digit == one:
            value += 1
        elif digit == two:
            value += 2
        elif digit == three:
            value += 3
        elif digit == four:
            value += 4
        elif digit == five:
            value += 5
        elif digit == six:
            value += 6
        elif digit == seven:
            value += 7
        elif digit == eight:
            value += 8
        elif digit == nine:
            value += 9
    
    return value

with open('day08/input.txt', 'r') as f:
    count = 0
    for line in f:
        count += decode(line)
    print(count)
