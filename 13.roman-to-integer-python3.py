# @leet start
class Solution:
    map_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        total = 0
        s = [i for i in s]
        while s:
            l = s.pop(0)
            if l in "IXC" and len(s) > 0 and s[0] != l:
                val = self.map_values.get(l, 0)
                # print(f"diminuindo {val} {l} proximo {s[0]}")
                if l == "I" and s[0] in ["V", "X"]:
                    total -= val
                elif l == "X" and s[0] in ["L", "C"]:
                    total -= val
                elif l == "C" and s[0] in ["D", "M"]:
                    total -= val
                else:
                    # print(f"aumentado {val} atual={l} proximo {s[0]}")
                    total += val
            else:
                val = self.map_values.get(l, 0)
                # print(f"aumentado {val}")
                total += val
        return total


# @leet end
