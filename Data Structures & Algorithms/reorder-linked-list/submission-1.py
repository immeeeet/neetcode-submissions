# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None

        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        cr2 = prev
        cr1 = head
        while cr1 and cr2:
            nxt1 = cr1.next
            nxt2 = cr2.next

            cr1.next = cr2
            cr1 = nxt1
            cr2.next = cr1
            cr2 = nxt2