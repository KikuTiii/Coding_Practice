from collections import deque


class MovingAverage:
    def __init__(self, size: int):
            self.queue = deque()
            self.size = size
            self.current_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.current_sum += val

        if len(self.queue) > self.size:
            old = self.queue.popleft()
            self.current_sum -= old
        return self.current_sum / len(self.queue)


moving = MovingAverage(3)

assert moving.next(1) == 1.0
assert moving.next(10) == 5.5
assert abs(moving.next(3) - 4.666666666666667) < 1e-9
assert moving.next(5) == 6.0

moving2 = MovingAverage(2)

assert moving2.next(4) == 4.0
assert moving2.next(8) == 6.0
assert moving2.next(10) == 9.0

print("Todos os testes passaram!")