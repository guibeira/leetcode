# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        if head is None:
            return True
        ele = []
        nxt = head

        while nxt:
            ele.append(nxt)
            nxt = nxt.next
            length += 1

        middle = int(length / 2)
        first_part = ele[:middle]
        second_part = ele[middle:]
        first_val = [i.val for i in first_part]
        second_val = [i.val for i in second_part]
        second_val.reverse()
        for i, val in enumerate(first_val):
            s = second_val[i]
            if val != s:
                return False
        return True


# @leet end
