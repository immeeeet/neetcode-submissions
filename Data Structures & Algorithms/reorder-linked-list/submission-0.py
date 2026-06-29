# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #Now slow is in middle
        temp = slow.next
        slow.next = None
        
        prev = None

        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        
        while prev and curr:
            nxt1 = curr.next
            nxt2 = prev.next

            curr.next = prev
            prev.next = nxt1
            prev = nxt2
            curr = nxt1