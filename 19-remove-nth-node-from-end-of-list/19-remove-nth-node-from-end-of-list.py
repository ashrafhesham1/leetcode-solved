class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        def listLen(head: ListNode) -> int:
            pointer = head
            size = 0
            while pointer:
                size += 1
                pointer = pointer.next
            return size

        size = listLen(head)


        if size == 1: return None
        if n == size: return head.next

        pointer = head
        for i in range(size):
            if i == size - n -1 :
                pointer.next = pointer.next.next if pointer.next.next else None
            else:
                pointer = pointer.next
        return head