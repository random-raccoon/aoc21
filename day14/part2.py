import re

# Okay.  SLL is not going to scale.
# Back of napkin calculations give:
# start length 20, 2^40 growth factor, ~20 trillion.
# Just for storage (forget calculations) we are out of memory.
# SO.  Dynamic programming time.

# Rough thoughts:  Each pair expands into a tree.  Each tree can be summarized with a count.
# Tree counts need to account for depth.
# Take (a, b) and rule (a, b) -> c.
# count((a,b), n) = count((a,c), n-1) + count((c,b), n-1) + {c:-1}.
# Take (a, b) without any matching rules.
# count((a, b), n) = {a:1, b:1}
# And finally:
# count((a, b), 0) = {a:1, b:1}
# Map of pairs of elements to the new element that will get injected between them.
rules = {}

# Map of (element1, element2, depth) tuples to their {element:count} maps.
cache = {}

# Merges count2's values into count1.
def merge(count1, count2):
    for key, value in count2.items():
        count1[key] = count1.get(key, 0) + value

# Calculates the {element:count} map for a tree starting at (element1,element2) going to a depth of depth.
def calculate(element1, element2, depth):
    if ((element1, element2, depth)) in cache:
        return cache[(element1, element2, depth)]

    if depth == 0 or (element1, element2) not in rules:
        retval = {element1: 1}
        merge(retval, {element2: 1})  # Ugly, but handles element1 == element2 in one line.
        return retval

    count = {}
    new_element = rules[(element1, element2)]

    merge(count, calculate(element1, new_element, depth - 1))
    merge(count, calculate(new_element, element2, depth - 1))
    merge(count, {new_element: -1})  # correct for double-counting new_element.

    cache[(element1, element2, depth)] = count
    return count

with open('day14/input.txt', 'r') as f:
    sequence = f.readline().strip()

    _ = f.readline()  # empty line

    rules = {(pair[0],pair[1]):new_element for [pair, new_element] in [re.split(' -> ', line.strip()) for line in f.readlines()]}

    count = {}
    depth = 40
    for i in range(0, len(sequence) - 1):
        merge(count, calculate(sequence[i], sequence[i+1], depth))

    # Correct for double-counted internal values:
    for i in range(1, len(sequence) - 1):
        merge(count, {sequence[i]: -1})

    # And the answer is the max vs the min.
    max_element = max(count, key=count.get)
    min_element = min(count, key=count.get)

    print(count[max_element] - count[min_element])