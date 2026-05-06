# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #####################################################
        # brute force
        #####################################################
        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # i, j = 0, len(nodes) - 1

        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i += 1
        #     nodes[j].next = nodes[i]
        #     j -= 1
        
        # nodes[i].next = None

        #####################################################
        # reverse and join
        #####################################################

        # find the middle using fast and slow pointers

        slow = head
        fast = head
        # find the middle portion and end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # middle portion
        second_half = slow.next
        
        # reverse the second half.  {1 -> 2 -> 3} => {3 -> 2 -> 1}
        prev = slow.next = None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp

        # merge the two lists
        first, second = head, prev

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            first.next.next = tmp1
            second = tmp2
            first = tmp1
            
        
















        