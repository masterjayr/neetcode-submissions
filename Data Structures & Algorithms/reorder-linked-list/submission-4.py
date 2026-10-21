# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        curr, prev = slow, None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        curr, prev = head, prev

        while prev and prev.next:
            next = curr.next
            next2 = prev.next
            curr.next = prev
            prev.next = next
            curr = next
            prev = next2