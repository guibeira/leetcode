# @leet start
import collections


class Solution:
    def bfs(self, r, c, row, col, board, visited):
        q = collections.deque()
        q.append((r, c))
        visited.add((r, c))
        directions = [
            (-1, 0),  # left
            (0, 1),  # up
            (1, 0),  # right
            (0, -1),  # down
        ]
        while q:
            r, c = q.popleft()
            visited.add((r, c))
            for dr, dc in directions:
                rw = r + dr
                cw = c + dc
                is_in_range_row = rw >= 0 and rw < row
                is_in_range_col = cw >= 0 and cw < col
                if (
                    is_in_range_row
                    and is_in_range_col
                    and board[rw][cw] == "O"
                    and (rw, cw) not in visited
                ):
                    q.append((rw, cw))

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        visited = set()
        # for rw in board:
        #     print(rw)

        # top line
        for c in range(col):
            if board[0][c] == "O" and (0, c) not in visited:
                self.bfs(0, c, row, col, board, visited)
        # botton line
        last_row = row - 1
        for c in range(col):
            if board[last_row][c] == "O" and (last_row, c) not in visited:
                self.bfs(last_row, c, row, col, board, visited)
        # left collum
        for r in range(row):
            if board[r][0] == "O" and (r, 0) not in visited:
                self.bfs(r, 0, row, col, board, visited)
        # right collum
        last_col = col - 1
        for r in range(row):
            if board[r][last_col] == "O" and (r, last_col) not in visited:
                self.bfs(r, last_col, row, col, board, visited)

        # update the board
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"


# @leet end
