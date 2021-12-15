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
        return self.__explore([], 'start', False)

    def __explore(self, path: list[str], next_cave: str, has_second_visit: bool) -> int:
        count = 0
        for cave in self.caves[next_cave]:
            if cave == 'end':
                p = path.copy()
                p.append('end')
                print(','.join(p))
                count += 1
            elif cave == 'start':
                # no leaving the cave.
                continue
            elif cave.islower() and cave in path:
                if has_second_visit:
                    continue
                else:
                    count += self.__explore(path.copy(), cave, True)
            else:
                count += self.__explore(path.copy(), cave, has_second_visit)
        return count

with open('day12/input.txt', 'r') as f:
    network = CaveNetwork()
    for line in f:
        parts = line.strip().split('-')
        network.add_tunnel(parts[0], parts[1])
    
    print(network.count_paths())
