# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode() # ListNode() form
        current = dummy 

        pointer1 = list1
        pointer2 = list2

        while pointer1 and pointer2: # if both two have left nodes
            if pointer1.val <= pointer2.val:
                current.next = pointer1
                pointer1 = pointer1.next
            else:
                current.next = pointer2
                pointer2 = pointer2.next

            current = current.next

        if pointer1:
            current.next = pointer1
        else:
            current.next = pointer2

        return dummy.next
