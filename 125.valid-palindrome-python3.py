# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(filter(str.isalnum, s))
        r = list(s)
        r.reverse()

        while s:
            first = s.pop()
            last = r.pop()
            if first != last:
                return False
        return True


# @leet end
