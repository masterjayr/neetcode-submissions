# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)

        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)

            if not kth:
                break

            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, head, k):
        curr = head
        while k > 0 and curr:
            curr = curr.next
            k -= 1

        return curr