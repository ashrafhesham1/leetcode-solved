class Solution:
    
    def _hasCycle(self, head: ListNode, visited ) -> bool:

        if head in visited : return True
        visited.append(head)
        if head.next : return self._hasCycle(head.next,visited)
        return False

    def hasCycle(self, head: ListNode) -> bool:
        if not head : return False
        return self._hasCycle(head,[])