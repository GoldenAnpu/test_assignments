# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        check_list = []
        new_head = head
        while head.next:
            check_list.append(head.val)
            head = head.next
        check_list.append(head.val)
        while len(check_list) > 1:
            last = check_list.pop(-1)
            first = check_list.pop(0)
            if last != first:
                return False
        return True
