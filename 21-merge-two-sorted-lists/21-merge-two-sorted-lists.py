# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res_list = ListNode()
        res_list_pointer = res_list

        while list1 != None and list2 != None :
            if list1.val < list2.val :
                res_list_pointer.next = ListNode(list1.val)
                list1 = list1.next
            else:
                res_list_pointer.next = ListNode(list2.val)
                list2 = list2.next

            res_list_pointer = res_list_pointer.next

        while list1 != None :
            res_list_pointer.next = ListNode(list1.val)
            res_list_pointer = res_list_pointer.next
            list1 = list1.next

        while list2 != None :
            res_list_pointer.next = ListNode(list2.val)
            res_list_pointer = res_list_pointer.next
            list2 = list2.next

        res_list = res_list.next
        
        return res_list