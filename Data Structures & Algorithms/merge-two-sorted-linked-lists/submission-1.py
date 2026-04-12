# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list cases
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        #Find list with lowest starting val

        smol = None
        big = None
        
        if list1.val <= list2.val:
            smol = list1
            big = list2
        else:
            smol = list2
            big = list1

        
        head = curr = ListNode(0,None)
        
        while smol and big:
            if smol.val < big.val:
                curr.next = smol
                smol = smol.next
            else:
                curr.next = big
                big = big.next
            curr = curr.next 
        
        if not smol:
            curr.next = big
        else:
            curr.next = smol

        return  head.next