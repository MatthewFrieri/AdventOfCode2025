from collections import defaultdict
from datetime import datetime
import itertools

import pandas as pd
import tqdm
from base_answer import BaseAnswer

class PartOne(BaseAnswer):


    def find_splitters(data: list[str]):

        splitters = []
        for i, row in enumerate(list(data)):
            for j, item in enumerate(row):
                if item == "^":
                    splitters.append((i,j))

        return splitters

    @classmethod
    def answer(cls, data: list[str]):

        splitters = cls.find_splitters(data)

        non_spliiters = []
        for i, j in splitters:
            splitter_on_side = False
            for k in range(i-1, -1, -1):
                if (k, j+1) in splitters or (k, j-1) in splitters:
                    splitter_on_side = True
                if (k, j) in splitters:
                    if not splitter_on_side:
                        non_spliiters.append((i, j))
                    break
        
        return len(splitters) - len(non_spliiters)


class PartTwo(PartOne):

    @classmethod
    def build_tree(cls, data: list[str]):

        height, width = len(data), len(data[0])
        splitters = cls.find_splitters(data)
        splitters += [(height, j) for j in range(width)]

        # directed tree
        adj_list = defaultdict(list)
        for i, j in splitters:
            low_i = i
            while low_i > 1:
                low_i -= 2
                if (low_i, j) in splitters:
                    break
                if (low_i, j-1) in splitters:
                    adj_list[(low_i, j-1)].append((i, j))
                if (low_i, j+1) in splitters:
                    adj_list[(low_i, j+1)].append((i, j))
        return adj_list, splitters[0]

    @classmethod
    def traverse(cls, tree: dict, start: tuple, memo: dict):
        # Return the number of paths of the tree starting at start
        total = 0
        for child in tree[start]:
            total += memo[child] if child in memo else cls.traverse(tree, child, memo)
        memo[start] = 1 if total == 0 else total
        return memo[start]

    @classmethod
    def answer(cls, data: list[str]):

        # data = [
        #     ".......S.......",
        #     "...............",
        #     ".......^.......",
        #     "...............",
        #     "......^.^......",
        #     "...............",
        #     ".....^.^.^.....",
        #     "...............",
        #     "....^.^...^....",
        #     "...............",
        #     "...^.^...^.^...",
        #     "...............",
        #     "..^...^.....^..",
        #     "...............",
        #     ".^.^.^.^.^...^.",
        #     "...............",
        # ]

        tree, start = cls.build_tree(data)
        # tree = defaultdict(list, itertools.islice(tree.items(), 10))
        return cls.traverse(tree, start, {})
            

# PartOne.run(7)
PartTwo.run(7)
