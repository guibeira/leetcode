# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(filter(str.isalnum, s))
        # r = list(s)
        # r.reverse()

        # while s:
        #     first = s.pop()
        #     last = r.pop()
        #     if first != last:
        #         return False
        # return True
        r_index = len(s) - 1
        l_index = 0

        for _ in range(len(s)):
            if s[l_index] != s[r_index]:
                return False
            # case where we cover all the letters
            if l_index > r_index:
                break
            l_index += 1
            r_index -= 1
        return True


# @leet end
