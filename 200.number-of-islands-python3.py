# @leet start
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            # island_cordenates = []
            while q:
                row, col = q.popleft()
                # island_cordenates.append((row, col))
                directions = [
                    (-1, 0),  # left
                    (0, 1),  # up
                    (1, 0),  # right
                    (0, -1),  # down
                ]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    r_in_range = r in range(rows)
                    c_in_range = c in range(cols)
                    not_visited = (r, c) not in visit
                    if r_in_range and c_in_range and grid[r][c] == "1" and not_visited:
                        q.append((r, c))
                        visit.add((r, c))
            # return island_cordenates

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    # print(island_cordenates)
                    island += 1
        # for row in grid:
        #     print(row)
        return island


# @leet end
