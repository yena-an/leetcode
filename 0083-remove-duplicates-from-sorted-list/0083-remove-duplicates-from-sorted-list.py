# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        dummy = ListNode()
        current = dummy

        pointer1 = head
        pointer2 = head.next

        while pointer2:
            if pointer1.val != pointer2.val:
                current.next = pointer1
                current = current.next

            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        current.next = pointer1
        current.next.next = None

        return dummy.next
