from base_answer import BaseAnswer
from bisect import bisect_right


class PartOne(BaseAnswer):

    def answer(data: list[str]):
        intervals, querries = [x.strip() for x in data]

        intervals = [tuple([int(x) for x in interval.split("-")]) for interval in intervals.split("\n")]
        intervals.sort()

        # Remove subset intervals

        to_keep = []
        for i, interval in enumerate(intervals):
            if i == len(intervals) - 1 or intervals[i + 1][0] != interval[0]:
                to_keep.append(interval)
        intervals = list(set(intervals).intersection(set(to_keep)))
        intervals.sort()

        to_keep = []
        for i in range(len(intervals) - 1, -1, -1):
            i = len(intervals) - i - 1
            if i == 0 or not (intervals[i - 1][0] != intervals[i][0] and intervals[i - 1][1] >= intervals[i][1]):
                to_keep.append(intervals[i])
        intervals = list(set(intervals).intersection(set(to_keep)))
        intervals.sort()

        # Run querries

        valid = 0
        lefts = [x[0] for x in intervals]
        for q in querries.split("\n"):
            q = int(q.strip())

            idx = bisect_right(lefts, q) - 1
            valid += q <= intervals[idx][1]

        return valid


class PartTwo(BaseAnswer):

    def answer(data: list[str]):
        intervals, querries = [x.strip() for x in data]

        intervals = [tuple([int(x) for x in interval.split("-")]) for interval in intervals.split("\n")]
        intervals.sort()

        # Remove subset intervals

        to_keep = []
        for i, interval in enumerate(intervals):
            if i == len(intervals) - 1 or intervals[i + 1][0] != interval[0]:
                to_keep.append(interval)
        intervals = list(set(intervals).intersection(set(to_keep)))
        intervals.sort()

        to_keep = []
        for i in range(len(intervals) - 1, -1, -1):
            i = len(intervals) - i - 1
            if i == 0 or not (intervals[i - 1][0] != intervals[i][0] and intervals[i - 1][1] >= intervals[i][1]):
                to_keep.append(intervals[i])
        intervals = list(set(intervals).intersection(set(to_keep)))
        intervals.sort()

        # Flatten intervals

        extra = len([x for x in intervals if x[0] == x[1]])

        flattened = []
        for interval in intervals:
            flattened += [("L", interval[0]), ("R", interval[1])]

        bounds = [x[1] for x in flattened]
        flattened = [x for x in flattened if bounds.count(x[1]) == 1]
        flattened.sort(key=lambda x: x[1])

        # Count interval lengths

        count = 0
        left_bound = None
        imbalance = 0
        for pair in flattened:
            side, bound = pair
            imbalance += -1 if side == "L" else 1

            if side == "L" and imbalance == -1:
                left_bound = bound
            if side == "R" and imbalance == 0:
                count += bound - left_bound + 1
        return count + extra


PartOne.run(5, split_on="\n\n")
PartTwo.run(5, split_on="\n\n")
