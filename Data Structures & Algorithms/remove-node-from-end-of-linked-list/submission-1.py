# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # find the size ot the linked list and remove from
        # beginning instead
        size = 0
        temp = head

        while temp:
            temp = temp.next
            size += 1

        if size - n == 0:
            return head.next

        curr = head
        i = 1
        while i < (size - n ):
            curr = curr.next
            i += 1

        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None

        return head
