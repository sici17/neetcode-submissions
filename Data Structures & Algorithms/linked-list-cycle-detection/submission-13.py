# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        currslow=head
        currfast=head

        while currfast and currfast.next:

            currfast=currfast.next.next
            currslow=currslow.next

            if currslow==currfast:
                return True
            
            
        
        return False








        