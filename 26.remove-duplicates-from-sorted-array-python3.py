# @leet start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_nr = {}

        for n in nums:
            nums_nr[n] = nums_nr.get(n, 0) + 1
        for num, amount in nums_nr.items():
            for i in range(amount - 1):
                nums.remove(num)

        nums


# @leet end
