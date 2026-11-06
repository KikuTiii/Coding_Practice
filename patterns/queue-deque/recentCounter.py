from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:

        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

counter = RecentCounter()

assert counter.ping(1) == 1
assert counter.ping(100) == 2
assert counter.ping(3001) == 3
assert counter.ping(3002) == 3

counter2 = RecentCounter()

assert counter2.ping(10) == 1
assert counter2.ping(3010) == 2
assert counter2.ping(6011) == 1

print("Todos os testes passaram!")