# You are given an array tickets, where tickets[i] is the number of tickets person i wants to buy.

# People are initially standing in a line from index 0 to n - 1.

# Every second:
# - the person at the front buys exactly one ticket;
# - if they still need more tickets, they move to the end of the line;
# - otherwise, they leave the line.
# Return how many seconds pass until person k finishes buying all their tickets.

# eu preciso guardar o indice da pessoa, toda vez que ela chegar ao topo da fila, ela compra um ticket e vai para o final da fila (caso ainda tenha tickets para comprar)
# quando ela comprar o ticket, eu decremento o numero de tickets restantes e a posiçao dela na fila
# k é a pessoa que queremos saber quanto tempo ela levou para comprar todos os tickets


from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:

        queue = deque(range(len(tickets)))
        seconds = 0

        while queue:
            i = queue.popleft()
            tickets[i] -= 1
            seconds += 1

            if tickets[i] == 0 and i == k:
                return seconds

            if tickets[i] > 0:
                queue.append(i)


solution = Solution()

assert solution.timeRequiredToBuy([2, 3, 2], 2) == 6
assert solution.timeRequiredToBuy([5, 1, 1, 1], 0) == 8
assert solution.timeRequiredToBuy([1], 0) == 1
assert solution.timeRequiredToBuy([1, 2], 1) == 3

print("Todos os testes passaram!")