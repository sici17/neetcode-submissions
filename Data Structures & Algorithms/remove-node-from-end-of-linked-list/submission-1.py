# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        curr=dummy
        curravanti=head

        while n>0:
            curravanti=curravanti.next 
            n-=1

        while curravanti:
            curravanti=curravanti.next
            curr=curr.next
        
        curr.next=curr.next.next

        return dummy.next
        

               



        