# @leet start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = Counter(s)
        tc = Counter(t)

        if len(sc.keys()) != len(tc.keys()):
            return False

        for k in sc.keys():
            if k not in tc.keys():
                return False
            if sc[k] != tc[k]:
                return False

        return True


# @leet end
