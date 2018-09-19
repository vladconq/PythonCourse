import random
from collections import defaultdict


class Graph:
    def __init__(self, E):
        self.E = E
        self.root = random.choice(list(self.E.keys()))


class GraphIterator:
    def __init__(self, g):
        self.graph = g
        self.used = defaultdict(bool)  # returns False by default
        self.used[self.graph.root] = True
        self.queue = [self.graph.root]

    def hasNext(self) -> bool:
        return bool(len(self.queue))

    def __next__(self) -> str:
        if self.hasNext():
            element = self.queue.pop(0)
            for child in self.graph.E[element]:
                if not self.used[child]:
                    self.used[child] = True
                    self.queue.append(child)
            return element
        else:
            raise StopIteration

    def __iter__(self):
        return self


g = Graph({
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
})

result = []

for vertex in GraphIterator(g):
    result.append(vertex)

print(result)
