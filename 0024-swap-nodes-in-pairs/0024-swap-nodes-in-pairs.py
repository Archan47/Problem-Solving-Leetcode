# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        prev = head
        curr = head.next
        head = curr
        while True:
            nextNode = curr.next
            curr.next = prev
            if nextNode is None or nextNode.next is None:
                prev.next = nextNode
                break
            prev.next = nextNode.next
            prev = nextNode
            curr = prev.next
        return head



        