braces = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

braceValues = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

with open('day10/input.txt', 'r') as f:
    scores = []
    for line in f:
        stack = []
        corrupt = False
        for c in line.strip():
            if c in braces:
                stack.append(braces[c])
            elif len(stack) == 0:
                corrupt = True
                break
            else:
                want = stack.pop()
                if c != want:
                    corrupt = True
                    break

        if not corrupt and len(stack) != 0:
            # incomplete!
            score = 0
            stack.reverse()
            for c in stack:
                score *= 5
                score += braceValues[c]
            scores.append(score)
    
    scores.sort()
    print(scores[len(scores) // 2])
