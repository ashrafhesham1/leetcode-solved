class Solution:

    def swapPairs(self, head: ListNode) -> ListNode :
        # 0 -> 1 -> 2 -> 3
        def swap (head):
            if not head.next or not head.next.next : return

            # stand on n - 1 elem
            # make a temp that point to n  elem          # temp -> 1
            temp = head.next #1
            # make the n - 1 elem point to the n + 1 elem       # 0 -> 2
            head.next = head.next.next #2
            # make the temp point to the n + 2 elem             # 1 -> 3
            temp.next = head.next.next
            # make the n + 2 elem point to the temp         # 2 -> 1
            head.next.next = temp
            # loop
            swap(head.next.next)

        if not head : return head

        dummy = ListNode(0,head)
        swap(dummy)
        return dummy.next