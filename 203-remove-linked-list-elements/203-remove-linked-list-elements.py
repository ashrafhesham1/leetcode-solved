# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        head = ListNode(0,head)
        pointer = head
        while pointer and pointer.next :
            if pointer.next.val == val :
                pointer.next = pointer.next.next
                continue
            pointer = pointer.next
        return head.next