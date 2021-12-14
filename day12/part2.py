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
        return self.__explore([], 'start')

    def __explore(self, path: list[str], next_cave: str) -> int:
        path.append(next_cave)
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
            elif cave.islower() and path.count(cave) == 2:
                # can't visit a small cave more than twice
                # NOPE.  Can visit ONE small cave twice.  Revisit this later.
                continue
            else:
                count += self.__explore(path.copy(), cave)
        return count

with open('day12/testinput.txt', 'r') as f:
    network = CaveNetwork()
    for line in f:
        parts = line.strip().split('-')
        network.add_tunnel(parts[0], parts[1])
    
    print(network.count_paths())
