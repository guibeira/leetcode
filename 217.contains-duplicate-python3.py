# @leet start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for k in counter.keys():
            if counter[k] > 1:
                return True


# @leet end
