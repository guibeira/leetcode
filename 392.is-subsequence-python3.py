# @leet start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # solution using dequeu
        # s = [i for i in s]
        # for l in t:
        #     if len(s) == 0:
        #         break
        #     if l == s[0]:
        #         s.pop(0)
        # return len(s) == 0

        # solution using two pointers
        amount_words = len(s)

        if amount_words == 1:
            return s in t
        if amount_words == 0:
            return True
        if amount_words > len(t):
            return False

        l_index = 0
        total_words = 0
        for w in t:
            if total_words == amount_words:
                return True
            if w == s[l_index]:
                l_index += 1
                total_words += 1

        return total_words == amount_words


# @leet end
