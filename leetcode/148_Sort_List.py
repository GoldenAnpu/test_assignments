# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        collector = []

        if not head:
            return head

        while head.next:
            collector.append(head.val)
            head = head.next
        collector.append(head.val)
        collector.sort()
        new_head = temp = ListNode()
        while collector:
            new_head.next = ListNode(collector.pop(0))
            new_head = new_head.next
        return temp.next