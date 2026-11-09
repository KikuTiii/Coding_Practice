# Given a binary array nums and an integer k, return the maximum number of consecutive 1s in
# the array if you can flip at most k zeros.

# A flip changes a 0 into a 1.

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros =  0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return max_length


# tests
solution = Solution()

assert solution.longestOnes(
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    2
) == 6

assert solution.longestOnes(
    [0, 0, 1, 1, 1, 0, 0],
    0
) == 3

assert solution.longestOnes(
    [0, 0, 0],
    2
) == 2

assert solution.longestOnes(
    [1, 1, 1, 1],
    2
) == 4

assert solution.longestOnes(
    [0, 1, 1, 0, 1, 1, 1, 0],
    1
) == 6

print("Todos os testes passaram!")