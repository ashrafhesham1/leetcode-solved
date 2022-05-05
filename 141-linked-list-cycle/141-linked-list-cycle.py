class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast : return True

        return False




'''
class Solution:
    
    def _hasCycle(self, head: ListNode, visited ) -> bool:

        if head in visited : return True
        visited.append(head)
        if head.next : return self._hasCycle(head.next,visited)
        return False

    def hasCycle(self, head: ListNode) -> bool:
        if not head : return False
        return self._hasCycle(head,[])
        
'''