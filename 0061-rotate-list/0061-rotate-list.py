# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        else:
            curr = head
            length = 1
            while curr.next:
                curr = curr.next
                length += 1
            print("curr points to ",curr.val)
            curr.next = head
            k = k % length
            steps_to_new_tail = length - k
            new_tail = head
            for _ in range(steps_to_new_tail - 1):
                new_tail = new_tail.next

# 4. Break the circle
            new_head = new_tail.next
            new_tail.next = None

            return new_head