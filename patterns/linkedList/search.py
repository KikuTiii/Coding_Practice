# Given the head of a singly linked list and an integer target, 
# return True if a node with value target exists in the list. Otherwise, return False.

# The linked list may be empty.

class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def contains(self, head: ListNode | None, target: int) -> bool:
        current = head

        while current:
            if current.val == target:
                return True
            current = current.next
        return False


solution = Solution()

# 5 -> 10 -> 15 -> 20
head = ListNode(5)
head.next = ListNode(10)
head.next.next = ListNode(15)
head.next.next.next = ListNode(20)

assert solution.contains(head, 15) is True
assert solution.contains(head, 5) is True
assert solution.contains(head, 20) is True
assert solution.contains(head, 99) is False

# Empty list
assert solution.contains(None, 10) is False

# Single node
single = ListNode(7)
assert solution.contains(single, 7) is True
assert solution.contains(single, 3) is False

print("Todos os testes passaram!")