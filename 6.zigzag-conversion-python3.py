# @leet start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        amount = len(s)
        matrix = [[0] * amount for _ in range(numRows)]
        letters = [i for i in s]

        row = 0
        col = 0

        while letters:
            l = letters.pop(0)
            # for r in matrix:
            #     print(r)

            if row == numRows:
                col += 1
                row -= 2

            # logic for zigzag
            if col % (numRows - 1) == 0:
                matrix[row][col] = l
                row += 1
                continue
            else:
                # move to next collumn and decrement row
                matrix[row][col] = l
                row -= 1
                col += 1

        word = ""
        for r in matrix:
            for c in r:
                if c != 0:
                    word += c
        return word


# @leet end
