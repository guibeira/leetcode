# @leet start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            n_start, n_end = newInterval
            i_start, i_end = intervals[i]

            if i_start > n_end:  # newInterval is before current interval
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            elif n_start > i_end:  # newInterval is after current interval
                result.append(intervals[i])

            else:
                # newInterval overlaps with current interval
                newInterval[0] = min(n_start, i_start)
                newInterval[1] = max(n_end, i_end)

        result.append(newInterval)
        return result


# @leet end
