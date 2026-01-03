import math
import itertools

from base_answer import BaseAnswer


class DisjointSet:

    def __init__(self, items):
        self.rep = {k: k for k in items}

    def find_rep(self, item):
        if item == self.rep[item]:
            return item
        self.rep[item] = self.find_rep(self.rep[item])
        return self.rep[item]
    
    def union(self, item1, item2):
        rep1 = self.find_rep(item1)
        rep2 = self.find_rep(item2)
        self.rep[rep1] = rep2

    def get_sizes(self):
        values = [self.find_rep(item) for item in self.rep]
        reps = list(set(values))
        return sorted([values.count(rep) for rep in reps], reverse=True)
    
    def is_fully_connected(self):
        return len(self.get_sizes()) == 1


class PartOne(BaseAnswer):

    def get_distances(data: list[str]):
        coords = [tuple(int(y) for y in x.split(",")) for x in data if x]

        disjoint_set = DisjointSet(coords)
        pairs = itertools.combinations(coords, 2)

        return sorted(pairs, key=lambda pair: math.dist(*pair)), disjoint_set

    @classmethod
    def answer(cls, data: list[str]):
        distances, disjoint_set = cls.get_distances(data)

        for c1, c2 in distances[:1000]:
            disjoint_set.union(c1, c2)

        sizes = disjoint_set.get_sizes()
        return math.prod(sizes[:3])
    

class PartTwo(PartOne):

    @classmethod
    def answer(cls, data: list[str]):
        distances, disjoint_set = cls.get_distances(data)

        while not disjoint_set.is_fully_connected():
            c1, c2 = distances.pop(0)
            disjoint_set.union(c1, c2)

        return c1[0] * c2[0]


PartOne.run(8)
PartTwo.run(8)
