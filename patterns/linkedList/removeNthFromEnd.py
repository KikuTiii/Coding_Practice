# Given the head of a singly linked list and an integer n, remove the nth node from the end of the
# list and return the head of the resulting list.
# n is always valid.

class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int ) -> ListNode | None:

        dummy = ListNode(0)
        dummy.next = head

        current = head
        lenght = 0

        while current:
            lenght += 1
            current = current.next

        target_index = lenght - n
        current = dummy

        for _ in range(target_index):
            current = current.next
        current.next = current.next.next
        return dummy.next
            



# Tests
def build_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


solution = Solution()


head = build_list([1, 2, 3, 4, 5])
result = solution.removeNthFromEnd(head, 2)
assert to_list(result) == [1, 2, 3, 5]


head = build_list([1])
result = solution.removeNthFromEnd(head, 1)
assert to_list(result) == []


head = build_list([1, 2])
result = solution.removeNthFromEnd(head, 1)
assert to_list(result) == [1]


head = build_list([1, 2])
result = solution.removeNthFromEnd(head, 2)
assert to_list(result) == [2]


head = build_list([10, 20, 30, 40])
result = solution.removeNthFromEnd(head, 4)
assert to_list(result) == [20, 30, 40]


print("Todos os testes passaram!")