from base_answer import BaseAnswer


class PartOne(BaseAnswer):

    def answer(data: list[str]):
        joltage = 0
        for bank in data:
            first = "0"
            second = "0"
            prev_first = "0"

            for n in bank:
                if n > first:
                    prev_first = first
                    first = n
                    second = "0"
                elif n > second:
                    second = n
            joltage += int(prev_first + first) if second == "0" else int(first + second)
        return joltage


class PartTwo(BaseAnswer):

    @classmethod
    def max_joltage(cls, bank: str, n_batteries: int):
        if n_batteries == 1:
            return int(max(bank))
        potential_starts = cls.find_largests_with_remaining(bank, n_batteries - 1)
        largest_joltage = -1
        start_idx = None
        for idx in potential_starts:
            joltage = cls.max_joltage(bank[idx + 1 :], n_batteries - 1)
            if joltage > largest_joltage:
                start_idx = idx
                largest_joltage = joltage
        return int(bank[start_idx] + str(largest_joltage))

    def find_largests_with_remaining(bank: str, remaining: int):
        largest = "0"
        indices = []
        for i, n in enumerate(bank[:-remaining]):
            if n > largest:
                indices = [i]
                largest = n
            elif n == largest:
                indices.append(i)
        return indices

    @classmethod
    def answer(cls, data: list[str]):
        return sum([cls.max_joltage(bank, 12) for bank in data])


# PartOne.run(3)
PartTwo.run(3)
