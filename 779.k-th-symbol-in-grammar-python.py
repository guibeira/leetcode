# @leet start
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return self.builder(n, k)

    def builder(self, n, k):
        if n == 1:
            return 0
        if k <= 2 ** (n - 2):
            return self.builder(n - 1, k)
        else:
            return 1 - self.builder(n - 1, k - 2 ** (n - 2))


# @leet end
