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

    # Part 1 is just a single fold.
    (fold_dir, fold_coord) = folds[0]
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

    print(len(points))
