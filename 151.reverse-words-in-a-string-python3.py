# @leet start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        words.reverse()
        # print(words)
        result = " ".join(words)
        return result


# @leet end
