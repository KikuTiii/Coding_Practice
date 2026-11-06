# Given a sorted integer array nums and an integer target, return the index of the first occurrence of target. 
# If target does not exist, return -1.
# The array may contain duplicate values.

# o padrao usado é o binary search, quando encontrarmos o mid nao podemos retornar logo de primeira
# pois o mid pode nao ser a primeira ocorrencia


class Solution:
    def firstOccurrence(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result
 


solution = Solution()

assert solution.firstOccurrence([1, 2, 2, 2, 4, 5], 2) == 1
assert solution.firstOccurrence([1, 1, 1, 1], 1) == 0
assert solution.firstOccurrence([1, 3, 5, 7], 5) == 2
assert solution.firstOccurrence([1, 3, 5, 7], 4) == -1
assert solution.firstOccurrence([], 3) == -1

print("Todos os testes passaram!")