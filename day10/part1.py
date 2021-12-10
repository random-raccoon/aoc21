braces = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

errorValues = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

with open('day10/input.txt', 'r') as f:
    errorScore = 0
    for line in f:
        stack = []
        for c in line.strip():
            if c in braces:
                stack.append(braces[c])
            elif len(stack) == 0:
                errorScore += errorValues[c]
                break
            else:
                want = stack.pop()
                if c != want:
                    errorScore += errorValues[c]
                    break

    print(errorScore)
