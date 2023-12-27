# @leet start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [x[0] for x in counter.most_common(k)]


# @leet end
