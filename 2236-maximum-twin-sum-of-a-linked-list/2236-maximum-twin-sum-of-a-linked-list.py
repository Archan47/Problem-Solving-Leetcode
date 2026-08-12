# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        right = prev
        left = head

        maximum = 0
        while right:
            twinSum = left.val + right.val
            maximum = max(maximum, twinSum)
            left = left.next
            right = right.next
        return maximum
        