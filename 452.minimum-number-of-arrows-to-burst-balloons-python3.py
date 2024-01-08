# @leet start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        # print(f"points={points}")

        shots = [points[0][1]]
        prev = points[0][1]

        for balon in points:
            start, end = balon
            if start <= prev and end >= prev:
                # acertou
                continue
            else:
                shots.append(end)
                prev = end
        # print(f"shots: {shots}")
        return len(shots)


# @leet end
