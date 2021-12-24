import re

with open('day22/input.txt') as f:
    data = [0] * 101 * 101 * 101

    p = re.compile('(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
    for line in f:
        m = p.match(line.strip())
        (op, x1, x2, y1, y2, z1, z2) = m.groups()
        if op == 'on':
            op = 1
        else:
            op = 0
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        z1 = int(z1)
        z2 = int(z2)

        if x1 <= 50 and x2 >= -50 and y1 <= 50 and y2 >= -50 and z1 <= 50 and z2 >= -50:
            for z in range(z1, z2+1):
                z_index = (z+50) * 101 * 101
                for y in range(y1, y2+1):
                    y_index = (y+50) * 101
                    for x in range(x1, x2+1):
                        x_index = x+50
                        data[z_index + y_index + x_index] = op

    print(sum(data))