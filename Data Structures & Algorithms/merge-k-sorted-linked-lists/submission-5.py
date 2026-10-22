# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        
        if not lists:
            return None

        while len(lists) > 1:

            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i] if i >= 0 else None
                l2 = lists[i+1] if i+1 < len(lists) else None

                mergedList.append(self.merge(l1, l2))

            lists = mergedList

        return lists[0]

    def merge(self, list1, list2):

        dummy = ListNode()
        res = dummy

        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next

        if list1:
            res.next = list1
        
        if list2:
            res.next = list2
        

        return dummy.next

            



       


        