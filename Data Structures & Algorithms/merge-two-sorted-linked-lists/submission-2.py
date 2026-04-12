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

        
        head = smol

        while smol.next != None and big != None:
            if smol.next.val > big.val:
                smol_temp = smol.next
                # Next node in small will be node form bif
                smol.next = big

                # progress big to next node
                big = big.next

                # Correct newlt inserted big node to point to the original smol node
                smol.next.next = smol_temp
            
                
            smol = smol.next

        # either smol.next == None or big is iterated through.
        
        if smol.next == None:
            smol.next = big
        
        return head
