# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:

            kth = self.getKth(groupPrev, k)

            if not kth:
                break

            nextGroup = kth.next
            groupNext = groupPrev.next

            curr, prev = groupPrev.next, kth.next

            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            groupPrev.next = kth
            groupPrev = groupNext

        return dummy.next

    def getKth(self, node, k):
        curr = node

        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
