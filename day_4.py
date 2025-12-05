from base_answer import BaseAnswer


class PartOne(BaseAnswer):

    def answer(data: list[str]):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        valid = 0
        for i, shelf in enumerate(data):
            for j, paper in enumerate(shelf):
                if paper != "@":
                    continue

                coords = [
                    (i + di, j + dj) for di, dj in offsets if 0 <= i + di < len(data) and 0 <= j + dj < len(shelf)
                ]
                adjacents = [list(data)[i_][j_] for i_, j_ in coords]
                if adjacents.count("@") < 4:
                    valid += 1
        return valid


class PartTwo(BaseAnswer):

    def answer(data: list[str]):
        data = [list(row) for row in data]
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        total_removed = 0

        while total_removed == 0 or removed > 0:
            # print("\n".join(["".join(row) for row in data]) + "\n")
            removed = 0

            for i, shelf in enumerate(data):
                for j, paper in enumerate(shelf):
                    if paper != "@":
                        continue

                    coords = [
                        (i + di, j + dj) for di, dj in offsets if 0 <= i + di < len(data) and 0 <= j + dj < len(shelf)
                    ]
                    adjacents = [data[i_][j_] for i_, j_ in coords]
                    if adjacents.count("@") < 4:
                        removed += 1
                        data[i][j] = "x"
            total_removed += removed

        return total_removed


PartOne.run(4)
PartTwo.run(4)
