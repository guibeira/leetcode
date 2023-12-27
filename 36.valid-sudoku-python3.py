# @leet start
from typing import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for r in board:
            has_duplicated = Counter(r)
            for key, value in has_duplicated.items():
                if key == ".":
                    continue
                if value > 1:
                    return False

        # check col
        for col in range(len(board)):
            col_itens = set()
            for row in range(len(board)):
                val = board[row][col]
                # print(val)
                if val == ".":
                    continue

                if val not in col_itens:
                    col_itens.add(val)
                else:
                    # print(f"duplicated val in col {val}")
                    return False

            # print("***")

        # check 3x3 box
        for start in range(3):
            line = 0
            counter = set()
            for r in board:
                range_start = start * 3
                range_end = range_start + 3
                line += 1
                # print(r[range_start:range_end])
                for j in r[range_start:range_end]:
                    if j == ".":
                        continue
                    if j not in counter:
                        counter.add(j)
                    else:
                        # print(f"{j} esta duplicado")
                        return False

                if line == 3:
                    line = 0
                    counter = set()
        return True


# @leet end
