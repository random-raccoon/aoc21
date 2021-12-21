# oh wow.  all empty turns into all full.  Hacks abound.

def get(map, i, j, iteration_number):
    if i < 0 or i >= len(map):
        return iteration_number % 2
    if j < 0 or j >= len(map[i]):
        return iteration_number % 2
    return map[i][j]

def binary_to_dec(code):
    value = 0
    for c in code:
        value *= 2
        value += c
    return value

def resolve(map, rules, n):
    new_map = [[0 for i in range(len(map[0]) + 2)] for j in range(len(map) + 2)]

    for i in range(len(map)+2):
        for j in range(len(map[0])+2):
            code = [
                get(map, i-2, j-2, n), get(map, i-2, j-1, n), get(map, i-2, j, n),
                get(map, i-1, j-2, n), get(map, i-1, j-1, n), get(map, i-1, j, n),
                get(map, i  , j-2, n), get(map, i  , j-1, n), get(map, i  , j, n)]
            code_id = binary_to_dec(code)
            new_map[i][j] = rules[code_id]

    return new_map

def count_on(map):
    count = 0
    for row in map:
        for c in row:
            count += c
    return count

def display(map):
    for row in map:
        print(''.join(['#' if c == 1 else '.' for c in row]))

with open('day20/input.txt') as f:
    rules = [1 if c == '#' else 0 for c in f.readline().strip()]
    _ = f.readline()
    map = []
    for line in f:
        map.append([1 if c == '#' else 0 for c in line.strip()])

    for i in range(50):
        map = resolve(map, rules, i)

    print(count_on(map))