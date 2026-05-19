# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create one extra node
        dummy = ListNode(0, head)
        # assign left to start there
        left = dummy
        right = head

        # offset right by n -> basically the idea
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # move to end of list making left be at exactly
        # n from the end, but because of the dummy node
        # we are at n - 1 so we can point it to left.next.next
        while right:
            left = left.next
            right = right.next

        # technically deleting node at n by pointing n-1 to next.next
        left.next = left.next.next

        return dummy.next