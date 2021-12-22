# Player 1 starting position: 2
# Player 2 starting position: 10
rolls = 0
positions = [1, 9]  # offset by 1 to be 0 indexed.
scores = [0, 0]

def roll():
    global rolls
    rolls += 1
    return (rolls - 1) % 100 + 1

player = 0
while True:
    moves = roll() + roll() + roll()
    positions[player] = (positions[player] + moves) % 10
    scores[player] += positions[player] + 1
    if scores[player] >= 1000:
        print(f'Player {player + 1} wins!')
        print(f'result: {scores[(player+1)%2] * rolls}')
        break
    player = (player + 1) % 2