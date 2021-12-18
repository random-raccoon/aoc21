# Rather than taking input from a file this time, just put it in the code.
tx_min, tx_max = 153, 199
ty_min, ty_max = -114, -75

px, py = 0, 0
dx, dy = 18, 80

# Experimentation shows that 17,18,19 should hit for x.
# Since x and y are independent, doesn't matter which is chosen.
# The y values are a bit... ahem... hit and miss.

# Let us try math.
# yn = n * dy - n(n-1)/2
# Ugh.  Forget the math; this is rough enough to brute force.

def is_on_target():
    return px >= tx_min and px <= tx_max and py >= ty_min and py <= ty_max

def is_overshot():
    return py < ty_min and dy < 0

def step():
    global px, py, dx, dy
    px += dx
    py += dy
    if dx > 0:
        dx -= 1
    elif dx < 0:
        dx += 1
    dy -= 1


best_dy = 0
maxy = 0
for dy in range(1, 1000):
    dx = 18
    px, py = 0, 0
    current_maxy = 0
    while  not is_on_target() and not is_overshot():
        step()
        current_maxy = max(current_maxy, py)

    if is_on_target():
        if current_maxy > maxy:
            best_dy = dy
            maxy = current_maxy

print(f'{maxy} achieved with {dx}, {dy}')