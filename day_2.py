from base_answer import BaseAnswer


class PartOne(BaseAnswer):

    def is_invalid_id(id: str):
        if len(id) % 2 != 0:
            return False
        mid = len(id) // 2
        return id[:mid] == id[mid:]

    @classmethod
    def answer(cls, data: list[str]):
        id_sum = 0

        for id_range in data:
            start, end = id_range.split("-")
            
            for n in range(int(start), int(end) + 1):
                if cls.is_invalid_id(str(n)):
                    id_sum += n
            
        return id_sum


class PartTwo(PartOne):

    def is_invalid_id(id: str):
        n = len(id)
        for size in range(1, n // 2 + 1):
            if id == id[:size] * (n // size):
                return True
        return False


PartOne.run(2, split_on=",")
PartTwo.run(2, split_on=",")
