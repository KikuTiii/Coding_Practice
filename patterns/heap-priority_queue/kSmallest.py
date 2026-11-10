# Given an integer array nums and an integer k, return the k smallest elements in ascending order.

import heapq


class Solution:
    def kSmallest(self, nums: list[int], k: int) -> list[int]:

        heapq.heapify(nums)
        result = []

        for _ in range(k):
            smallest = heapq.heappop(nums)
            result.append(smallest)
        return result

# Tests
solution = Solution()

assert solution.kSmallest([7, 2, 5, 1, 9, 3], 3) == [1, 2, 3]
assert solution.kSmallest([4, 4, 2, 8, 1], 2) == [1, 2]
assert solution.kSmallest([10], 1) == [10]
assert solution.kSmallest([5, 3, 9, 1], 4) == [1, 3, 5, 9]

print("Todos os testes passaram!")