import re

# For fun, lets do this as a SLL!
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

with open('day14/input.txt', 'r') as f:
    sequence = f.readline().strip()
    head = Node(sequence[0])
    pointer = head
    for i in range(1, len(sequence)):
        node = Node(sequence[i])
        pointer.next = node
        pointer = node

    _ = f.readline()  # empty line

    rules = {(pair[0],pair[1]):new_element for [pair, new_element] in [re.split(' -> ', line.strip()) for line in f.readlines()]}

    # Apply the expansion rules.
    for i in range(40):
        size = 0
        pointer = head
        next = pointer.next
        while next != None:
            pair = (pointer.value, next.value)
            if pair in rules:
                new_element = Node(rules[pair])
                pointer.next = new_element
                new_element.next = next

            pointer = next
            next = pointer.next
            size += 1
        print(f'{i}, {size}')

    # Count the elements in the sequence
    count = {}
    pointer = head
    while pointer != None:
        count[pointer.value] = count.get(pointer.value, 0) + 1
        pointer = pointer.next

    # And the answer is the max vs the min.
    max_element = max(count, key=count.get)
    min_element = min(count, key=count.get)

    print(count[max_element] - count[min_element])