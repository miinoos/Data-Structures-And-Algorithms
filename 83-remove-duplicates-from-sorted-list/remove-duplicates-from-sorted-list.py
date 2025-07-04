# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        temp = head

        while temp is not None and temp.next is not None : 
            if temp.next.val == temp.val : 
                temp.next = temp.next.next
            else : 
                temp = temp.next
        
        
        return head