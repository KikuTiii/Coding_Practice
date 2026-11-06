# Given the head of a singly linked list and an integer target, remove every node whose value is
# equal to target and return the new head of the list.
# The head itself may need to be removed.


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
        self,
        head: ListNode | None,
        target: int
    ) -> ListNode | None:

        dummy = ListNode(0)
        dummy.next = head

        previous = dummy
        current = head

        while current:
            if current.val == target:
                previous.next = current.next
                current = current.next
            else:
                current = current.next
                previous = previous.next
        return dummy.next


def to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


solution = Solution()

# 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

result = solution.removeElements(head, 6)
assert to_list(result) == [1, 2, 3, 4, 5]

# Removing the head
head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(10)

result = solution.removeElements(head, 7)
assert to_list(result) == [10]

# Remove everything
head = ListNode(5)
head.next = ListNode(5)

result = solution.removeElements(head, 5)
assert to_list(result) == []

# Empty list
assert solution.removeElements(None, 3) is None

print("Todos os testes passaram!")