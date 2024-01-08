# @leet start
import heapq


class MinStack:
    def __init__(self):
        self.stack = []
        heapq.heapify(self.stack)

    def push(self, val: int) -> None:
        heapq.heappush(self.stack, val)

    def pop(self) -> None:
        return heapq.heappop(self.stack)

    def top(self) -> int:
        return heapq.nlargest(1, self.stack)[0]

    def getMin(self) -> int:
        return heapq.nsmallest(1, self.stack)[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end
