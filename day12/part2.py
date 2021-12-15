class Path:
    def __init__(self):
        self.caves = []
        self.has_second_visit = False
    
    def with_new_cave(self, cave: str):
        p = Path()
        p.has_second_visit = self.has_second_visit
        p.caves = self.caves.copy()
        p.caves.append(cave)
        return p

    def current_cave(self):
        return self.caves[len(self.caves)-1]

    def contains(self, cave):
        return cave in self.caves

class CaveNetwork:
    def __init__(self):
        self.caves = {}

    def add_tunnel(self, cave1: str, cave2: str):
        self.__add_cave(cave1)
        self.__add_cave(cave2)
        self.caves[cave1].add(cave2)
        self.caves[cave2].add(cave1)

    def __add_cave(self, cave: str):
        if not cave in self.caves:
            self.caves[cave] = set()

    def count_paths(self) -> int:
        count = 0

        start_path = Path()
        start_path.caves.append('start')
        paths = [start_path]

        while len(paths) > 0:
            path = paths.pop()
            cave = path.current_cave()
            for next_cave in self.caves[cave]:
                if next_cave == 'end':
                    # Made it out!  Record it.
                    count += 1
                elif next_cave == 'start':
                    # No leaving the cave this way.
                    continue
                elif next_cave.islower() and path.contains(next_cave):
                    if path.has_second_visit:
                        # No revisiting caves any more in this path.
                        continue
                    else:
                        next_path = path.with_new_cave(next_cave)
                        next_path.has_second_visit = True
                        paths.append(next_path)
                else:
                    next_path = path.with_new_cave(next_cave)
                    paths.append(next_path)

        return count


with open('day12/input.txt', 'r') as f:
    network = CaveNetwork()
    for line in f:
        parts = line.strip().split('-')
        network.add_tunnel(parts[0], parts[1])
    
    print(network.count_paths())
