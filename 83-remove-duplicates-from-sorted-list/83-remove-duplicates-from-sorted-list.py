# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pointer = head
        while pointer != None :
            if pointer.next != None :
                if pointer.val == pointer.next.val :
                    pointer.next = pointer.next.next
                    continue
            pointer = pointer.next
        return head