# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        cr1 = list1
        cr2 = list2
        ans = ListNode(None)
        c = ans
        while cr1!=None and cr2!=None:
            if cr1.val<=cr2.val:
                ans.next = cr1
                cr1 = cr1.next
            else:
                ans.next = cr2
                cr2 = cr2.next
            ans = ans.next
        if cr1==None:
            ans.next = cr2
        else:
            ans.next = cr1
        
        return c.next