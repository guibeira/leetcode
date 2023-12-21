# @leet start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        options = {}
        for word in strs:
            w = [i for i in word]
            w.sort()
            w = "".join(w)
            if w in options:
                options[w].append(word)
            else:
                options[w] = [word]
        return list(options.values())


# @leet end
