from base_answer import BaseAnswer

class PartOne(BaseAnswer):

    def answer(data):

        zeroes = 0
        tick = 50

        for rotation in data:
            direction = 1 if rotation[0] == "R" else -1
            change = int(rotation[1:])

            tick += change * direction
            tick %= 100

            if tick == 0:
                zeroes += 1

        return zeroes

class PartTwo(BaseAnswer):

    def answer(data):
        zeroes = 0
        tick = 50
        
        for rotation in data:
            direction = rotation[0]
            change = int(rotation[1:])

            if direction == "R":
                tick += change
                zeroes += tick // 100
                
            elif direction == "L":
                if tick == 0:
                    zeroes -= 1
                tick -= change
                zeroes += abs((tick - 1) // 100)

            tick %= 100

        return zeroes


PartOne.run(1)
PartTwo.run(1)
