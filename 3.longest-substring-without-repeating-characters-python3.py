# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        char_set = set()
        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
                max_len = max(max_len, r - l)
            else:
                char_set.remove(s[l])
                l += 1
        return max_len


# @leet end
