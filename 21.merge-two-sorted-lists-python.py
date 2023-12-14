# @leet start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        acc = ListNode()
        self.merge(list1, list2, acc)
        return acc.next

    def merge(self, d, u, acc):
        if d is None and u is None:
            return

        if d is None and u:
            acc.next = u
            acc = u
            return self.merge(d, u.next, acc)

        if u is None and d:
            acc.next = d
            acc = d
            return self.merge(d.next, u, acc)

        if d.val < u.val:
            acc.next = d
            acc = d
            return self.merge(u, d.next, acc)
        else:
            acc.next = u
            acc = u
            return self.merge(u.next, d, acc)


# @leet end
