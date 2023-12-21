# @leet start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = 0
        r = 0
        results = []
        for _ in range(len(nums)):
            if r + 1 > len(nums) - 1:
                n_start = nums[l]
                n_end = nums[r]
                if n_start == n_end:
                    results.append(str(n_start))
                else:
                    val = f"{n_start}->{n_end}"
                    results.append(val)
                break

            rn = nums[r]
            next = nums[r + 1]
            if next == rn + 1:
                r = r + 1
            else:
                n_start = nums[l]
                n_end = nums[r]
                if n_start == n_end:
                    results.append(str(n_start))
                else:
                    val = f"{n_start}->{n_end}"
                    results.append(val)
                l = r + 1
                r = r + 1
        return results


# @leet end
