# Player 1 starting position: 2
# Player 2 starting position: 10

# Well, this is different.  Clearly we can't evaluate *every* possible universe.
# Many universes will be effectively identical (eg. 2 + 2 + 2 = 1 + 2 + 3 = 3 + 2 + 1, etc)

universe_count_by_rolls = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}

# We now have a 7-way split instead of a 27-way one.  Is that enough?

# returns [number of times p1 wins, number of times p2 wins]
iters = 0
def solve(player, positions, scores, turn):
    # Just printing some progress markers; this algorithm is too slow :S
    global iters
    iters += 1
    if (iters % 1000000 == 0):
        print(iters)

    wins = [0,0]
    for (roll, count) in universe_count_by_rolls.items():
        new_positions = positions.copy()
        new_scores = scores.copy()
        new_positions[player] = (new_positions[player] + roll) % 10
        new_scores[player] += new_positions[player] + 1
        if new_scores[player] >= 21:
            wins[player] += count
        else:
            new_wins = solve((player + 1) % 2 , new_positions.copy(), new_scores.copy(), turn+1)
            wins[0] += count * new_wins[0]
            wins[1] += count * new_wins[1]
    return wins


rolls = 0
positions = [1, 9]  # offset by 1 to be 0 indexed.
scores = [0, 0]
wins = solve(0, positions, scores, 0)
print(wins)
print(max(wins))