# Given the head of a singly linked list, reverse the list and return its new head.

# You must reverse the links between the existing nodes.


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(
        self,
        head: ListNode | None
    ) -> ListNode | None:

        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


#Tests
def print_linked_list(head):
    current = head
    values = []

    while current:
        values.append(str(current.val))
        current = current.next

    if values:
        print(" -> ".join(values) + " -> None")
    else:
        print("None")


def to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result

solution = Solution()


# Test 1: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Teste 1 - Antes:")
print_linked_list(head)

result = solution.reverseList(head)

print("Teste 1 - Depois:")
print_linked_list(result)

assert to_list(result) == [4, 3, 2, 1]


# Test 2: single node
head = ListNode(7)

print("\nTeste 2 - Antes:")
print_linked_list(head)

result = solution.reverseList(head)

print("Teste 2 - Depois:")
print_linked_list(result)

assert to_list(result) == [7]


# Test 3: empty list
head = None

print("\nTeste 3 - Antes:")
print_linked_list(head)

result = solution.reverseList(head)

print("Teste 3 - Depois:")
print_linked_list(result)

assert result is None


# Test 4: two nodes
head = ListNode(10)
head.next = ListNode(20)

print("\nTeste 4 - Antes:")
print_linked_list(head)

result = solution.reverseList(head)

print("Teste 4 - Depois:")
print_linked_list(result)

assert to_list(result) == [20, 10]


# Test 5: longer list
head = ListNode(5)
head.next = ListNode(10)
head.next.next = ListNode(15)
head.next.next.next = ListNode(20)
head.next.next.next.next = ListNode(25)

print("\nTeste 5 - Antes:")
print_linked_list(head)

result = solution.reverseList(head)

print("Teste 5 - Depois:")
print_linked_list(result)

assert to_list(result) == [25, 20, 15, 10, 5]


print("\nTodos os testes passaram!")