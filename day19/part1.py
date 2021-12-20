# Oof.  This one seems challenging.

# Transformation matrix.
class Transform:
    def __init__(self, matrix=None):
        if matrix != None:
            self.matrix = matrix.copy()
        else:
            self.matrix = [
                1,0,0,0,
                0,1,0,0,
                0,0,1,0,
                0,0,0,1]

    def translate(self, translation):
        result = Transform(self.matrix)
        result.matrix[12] += translation[0]
        result.matrix[13] += translation[1]
        result.matrix[14] += translation[2]
        return result

    def mult(self, other):
        return Transform([
            self.matrix[0] * other.matrix[0] + self.matrix[1] * other.matrix[4] + self.matrix[2] * other.matrix[8] + self.matrix[3] * other.matrix[12],
            self.matrix[0] * other.matrix[1] + self.matrix[1] * other.matrix[5] + self.matrix[2] * other.matrix[9] + self.matrix[3] * other.matrix[13],
            self.matrix[0] * other.matrix[2] + self.matrix[1] * other.matrix[6] + self.matrix[2] * other.matrix[10] + self.matrix[3] * other.matrix[14],
            self.matrix[0] * other.matrix[3] + self.matrix[1] * other.matrix[7] + self.matrix[2] * other.matrix[11] + self.matrix[3] * other.matrix[15],

            self.matrix[4] * other.matrix[0] + self.matrix[5] * other.matrix[4] + self.matrix[6] * other.matrix[8] + self.matrix[7] * other.matrix[12],
            self.matrix[4] * other.matrix[1] + self.matrix[5] * other.matrix[5] + self.matrix[6] * other.matrix[9] + self.matrix[7] * other.matrix[13],
            self.matrix[4] * other.matrix[2] + self.matrix[5] * other.matrix[6] + self.matrix[6] * other.matrix[10] + self.matrix[7] * other.matrix[14],
            self.matrix[4] * other.matrix[3] + self.matrix[5] * other.matrix[7] + self.matrix[6] * other.matrix[11] + self.matrix[7] * other.matrix[15],

            self.matrix[8] * other.matrix[0] + self.matrix[9] * other.matrix[4] + self.matrix[10] * other.matrix[8] + self.matrix[11] * other.matrix[12],
            self.matrix[8] * other.matrix[1] + self.matrix[9] * other.matrix[5] + self.matrix[10] * other.matrix[9] + self.matrix[11] * other.matrix[13],
            self.matrix[8] * other.matrix[2] + self.matrix[9] * other.matrix[6] + self.matrix[10] * other.matrix[10] + self.matrix[11] * other.matrix[14],
            self.matrix[8] * other.matrix[3] + self.matrix[9] * other.matrix[7] + self.matrix[10] * other.matrix[11] + self.matrix[11] * other.matrix[15],

            self.matrix[12] * other.matrix[0] + self.matrix[13] * other.matrix[4] + self.matrix[14] * other.matrix[8] + self.matrix[15] * other.matrix[12],
            self.matrix[12] * other.matrix[1] + self.matrix[13] * other.matrix[5] + self.matrix[14] * other.matrix[9] + self.matrix[15] * other.matrix[13],
            self.matrix[12] * other.matrix[2] + self.matrix[13] * other.matrix[6] + self.matrix[14] * other.matrix[10] + self.matrix[15] * other.matrix[14],
            self.matrix[12] * other.matrix[3] + self.matrix[13] * other.matrix[7] + self.matrix[14] * other.matrix[11] + self.matrix[15] * other.matrix[15],
        ])

    def apply(self, beacon):
        return (
            beacon[0] * self.matrix[0] + beacon[1] * self.matrix[4] + beacon[2] * self.matrix[8] + self.matrix[12],
            beacon[0] * self.matrix[1] + beacon[1] * self.matrix[5] + beacon[2] * self.matrix[9] + self.matrix[13],
            beacon[0] * self.matrix[2] + beacon[1] * self.matrix[6] + beacon[2] * self.matrix[10] + self.matrix[14],
        )

    def __repr__(self):
        return (
            f'[{str(self.matrix[0]).rjust(2)}, {str(self.matrix[1]).rjust(2)}, {str(self.matrix[2]).rjust(2)}, {str(self.matrix[3]).rjust(2)}, \n'
            f' {str(self.matrix[4]).rjust(2)}, {str(self.matrix[5]).rjust(2)}, {str(self.matrix[6]).rjust(2)}, {str(self.matrix[7]).rjust(2)}, \n'
            f' {str(self.matrix[8]).rjust(2)}, {str(self.matrix[9]).rjust(2)}, {str(self.matrix[10]).rjust(2)}, {str(self.matrix[11]).rjust(2)}, \n'
            f' {str(self.matrix[12]).rjust(2)}, {str(self.matrix[13]).rjust(2)}, {str(self.matrix[14]).rjust(2)}, {str(self.matrix[15]).rjust(2)}]'
        )

# The 24 different orientations.
# I built this by writing down the 9 basic rotations, then writing a script
# that multiplied them together and found unique results.
standard_transforms = [
    Transform([0, -1, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 1]),
    Transform([0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]),
    Transform([-1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]),
    Transform([0, -1, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 1]),
    Transform([0, -1, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1]),
    Transform([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]),
    Transform([0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1]),
    Transform([0, 0, 1, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]),
    Transform([-1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]),
    Transform([-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1]),
    Transform([0, 0, -1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]),
    Transform([1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1]),
    Transform([0, 1, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 1]),
    Transform([0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]),
    Transform([1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1]),
    Transform([0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]),
    Transform([0, 0, -1, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]),
    Transform([0, 1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1]),
    Transform([0, 0, -1, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]),
    Transform([0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]),
    Transform([0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]),
    Transform([1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 1]),
    Transform([0, 0, 1, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1]),
    Transform([-1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 1])]

class Scanner:
    def __init__(self, name, beacons):
        self.name = name
        self.beacons = beacons

    def __repr__(self) -> str:
        return f'{self.name} with {len(self.beacons)} beacons'

    def beacons_with_transform(self, transform):
        return [transform.apply(beacon) for beacon in self.beacons]

def find_transform(scanner1, scanner2):
    print(f'comparing {scanner1.name} and {scanner2.name}')
    reference_beacons = set(scanner1.beacons)
    # Try all 24 transforms on scanner2 relative to scanner1.
    for transform in standard_transforms:
        # And try all translations that move each pair of points to the same location.
        for beacon1 in scanner1.beacons:
            for beacon2 in scanner2.beacons:
                diff = (beacon1[0] - beacon2[0], beacon1[1] - beacon2[1], beacon1[2] - beacon2[2])
                shifted_transform = transform.translate(diff)
                beacons = scanner2.beacons_with_transform(shifted_transform)
                overlap = reference_beacons.intersection(beacons)
                print(len(overlap))
                if len(overlap) >= 12:
                    print(f'found a match between {scanner1.name} and {scanner2.name}!')
                    # Woohoo!
                    return shifted_transform

    # Didn't find a match :(
    return None

scanners = []

with open('day19/testinput.txt') as f:
    need_name = True
    name = ''
    beacons = []
    for line in f:
        line = line.strip()
        if need_name:
            name = line
            need_name = False
        elif line == '':
            scanners.append(Scanner(name, beacons))
            beacons = []
            need_name = True
        else:
            beacons.append(tuple(int(n) for n in line.split(',')))
    scanners.append(Scanner(name, beacons))

# Find relative transforms between pairs of scanners where they exist.
transforms = {}
for i in range(len(scanners)):
    transforms[i] = []
    for j in range(i+1, len(scanners)):
        transform = find_transform(scanners[i], scanners[j])
        if transform != None:
            transforms[i].append((j, transform))

# do a traversal to set all global transforms.
world_transforms = {0: Transform()}
known = [0]
while len(known) > 0:
    i = known.pop()
    for (j, transform) in transforms[i]:
        if j not in world_transforms:
            world_transforms[j] = world_transforms[i].mult(transform)
            known.append(j)

# NOTE: assumption that this is fully solved at this point.

# using global transforms, populate world coordinates for beacons.
world_beacons = set()
for i in range(len(scanners)):
    world_beacons.update(scanners[i].beacons_with_transform(world_transforms[i]))

print(len(world_beacons))