import itertools
import numpy as np
from PIL import Image
import tifffile

from base_answer import BaseAnswer


class PartOne(BaseAnswer):

    def get_coords(data: list[str]):
        return [tuple(int(y) for y in x.split(",")) for x in data if x]

    def compute_area(c1: tuple[int, int], c2: tuple[int, int]):
        length = abs(c1[0] - c2[0]) + 1
        width = abs(c1[1] - c2[1]) + 1
        return length * width

    @classmethod
    def answer(cls, data: list[str]):

        coords = cls.get_coords(data)

        max_area = 0
        for c1, c2 in itertools.combinations(coords, 2):
            max_area = max(max_area, cls.compute_area(c1, c2))

        return max_area


class PartTwo(PartOne):

    def get_turn(a, b, c):
        v1 = (b[0] - a[0], b[1] - a[1])
        v2 = (c[0] - b[0], c[1] - b[1])
        cross_product = v1[0] * v2[1] - v1[1] * v2[0]
        return np.sign(cross_product)

    def is_coord_inside(c1, c2, coords):
        for coord in coords:
            if (min(c1[0], c2[0]) < coord[0] < max(c1[0], c2[0])) and (
                min(c1[1], c2[1]) < coord[1] < max(c1[1], c2[1])
            ):
                return True
        return False

    @classmethod
    def is_fully_outside(cls, c1, c2, coords, turns):
        i1 = coords.index(c1)
        i2 = coords.index(c2)

        if i1 > i2:
            i1, i2 = i2, i1

        seg1 = coords[i1 : i2 + 1]
        seg2 = coords[i2:] + coords[: i1 + 1]

        for seg in [seg1, seg2]:
            seg_turns = 0
            for i in range(len(seg) - 2):
                prev_coord = seg[i]
                coord = seg[i + 1]
                next_coord = seg[i + 2]
                seg_turns += cls.get_turn(prev_coord, coord, next_coord)

            if np.sign(seg_turns) != np.sign(turns):
                return True

        return False

    @classmethod
    def answer(cls, data: list[str]):

        # data = [
        #     "7,1",
        #     "11,1",
        #     "11,7",
        #     "9,7",
        #     "9,5",
        #     "2,5",
        #     "2,3",
        #     "7,3",
        # ]

        coords = cls.get_coords(data)
        wrapped_coords = coords + coords

        turns = 0

        for i in range(len(coords)):
            prev_coord = coords[i]
            coord = wrapped_coords[i + 1]
            next_coord = wrapped_coords[i + 2]
            turns += cls.get_turn(prev_coord, coord, next_coord)

        max_area = 0
        for c1, c2 in itertools.combinations(coords, 2):
            if cls.is_coord_inside(c1, c2, coords):
                continue
            if cls.is_fully_outside(c1, c2, coords, turns):
                continue

            max_area = max(max_area, cls.compute_area(c1, c2))

        return max_area


# PartOne.run(9)
res = PartTwo.run(9)

(14642, 83010)
(85036, 17904)
