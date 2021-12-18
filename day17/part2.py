# Rather than taking input from a file this time, just put it in the code.
tx_min, tx_max = 153, 199
ty_min, ty_max = -114, -75

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

px, py = 0, 0
dx, dy = 0,0

# I'm not proud.  But.. it does work.
count = 0
for check_dx in range(1, 250):
    print(check_dx)
    for check_dy in range(-200, 1000):
        dx = check_dx
        dy = check_dy
        px, py = 0, 0
        while True:
            step()
            if is_on_target():
                count += 1
                break
            if is_overshot():
                break
            if px < tx_min and dx == 0:
                break
            if px > tx_max and dy > 0:
                break

print(count)