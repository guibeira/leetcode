# @leet start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])

        print(f"Intervals : {intervals}")
        count_remove = 0

        prev = intervals[0]
        r = []
        for i in range(1, len(intervals)):
            print(f"Prev : {prev}")
            curr = intervals[i]

            c_start, c_end = curr
            p_start, p_end = prev

            if c_start >= p_start and p_end > c_start:
                count_remove += 1
                r.append(curr)
            else:
                prev[1] = curr[1]

        print(f"Remove : {r}")
        return count_remove


# @leet end
