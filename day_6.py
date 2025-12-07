from base_answer import BaseAnswer
import math
import re


class PartOne(BaseAnswer):

    def answer(data: list[str]):
        data = [list(filter(lambda y: y != "", x.split(" "))) for x in data[:-1]]

        n_problems = len(data[0])
        problem_size = len(data)

        transposed = []
        for i in range(n_problems):
            problem = []
            for j in range(problem_size):
                problem.append(data[j][i])
            transposed.append(problem)

        total = 0
        for problem in transposed:
            numbers, op = [int(x) for x in problem[:-1]], problem[-1]
            total += math.prod(numbers) if op == "*" else sum(numbers)
        return total


class PartTwo(BaseAnswer):

    def answer(data: list[str]):

        data = data[:-1]
        col_lengths = re.split(r"\+|\*", data[-1])[1:]
        col_lengths = [len(x) for x in col_lengths]
        col_lengths[-1] += 1
        cum_col_lengts = [sum(col_lengths[:i]) for i in range(len(col_lengths) + 1)]

        transposed = []
        for i in range(len(col_lengths)):
            problem = []
            for j in range(len(data)):
                start = cum_col_lengts[i] + i
                end = cum_col_lengts[i + 1] + i
                problem.append(data[j][start:end])
            transposed.append(problem)

        total = 0
        for problem in transposed:
            numbers, op = problem[:-1], problem[-1][0]
            new_numbers = []

            for i in range(len(numbers[0])):
                col = [number[i] for number in numbers]
                new_numbers.append(int("".join(col)))
            total += math.prod(new_numbers) if op == "*" else sum(new_numbers)
        return total


PartOne.run(6, progress_bar=False)
PartTwo.run(6, progress_bar=False)
