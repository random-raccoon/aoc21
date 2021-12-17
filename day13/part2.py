with open('day13/input.txt', 'r') as f:
    loading_points = True
    points = set()
    folds = []
    for line in f:
        if line.strip() == '':
            loading_points = False
        elif loading_points:
            [x, y] = line.strip().split(',')
            points.add((int(x),int(y)))
        else:
            [fold, coord] = line.strip().split('=')
            folds.append((fold[11], int(coord)))

    # Make the folds.
    for (fold_dir, fold_coord) in folds:
        new_points = set()
        if fold_dir == 'x':
            for (x, y) in points:
                if x >  fold_coord:
                    x = 2 * fold_coord - x
                new_points.add((x, y))
        elif fold_dir == 'y':
            for (x, y) in points:
                if y >  fold_coord:
                    y = 2 * fold_coord - y
                new_points.add((x, y))
        points = new_points

    # Draw the result.
    max_x, max_y = 0, 0
    for (x, y) in points:
        max_x, max_y = max(max_x, x), max(max_y, y)

    for y in range(0, max_y + 1):
        line = []
        for x in range(0, max_x + 1):
            if (x, y) in points:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))