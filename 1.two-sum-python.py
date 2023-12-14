# @leet start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx + 1 :]):
                if num + num2 == target:
                    return [idx, idx2 + idx + 1]


# @leet end
