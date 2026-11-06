class Solution:
    def hasPair(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return True

            if current_sum < target:
                left += 1
            else:
                right -= 1
        return False

solution = Solution()

assert solution.hasPair([1, 2, 4, 6, 10], 8) is True
assert solution.hasPair([1, 3, 5, 7], 10) is True
assert solution.hasPair([1, 3, 5, 7], 20) is False
assert solution.hasPair([2, 2], 4) is True
assert solution.hasPair([1], 2) is False
assert solution.hasPair([], 5) is False

print("Todos os testes passaram!")