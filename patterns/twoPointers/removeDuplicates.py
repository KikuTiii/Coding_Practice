# Given a sorted array nums, remove duplicates in-place so that each unique element appears only once. Return the number of unique elements.

# The relative order of the unique elements should remain the same.

# After your function returns k, the first k positions of nums must contain the unique values.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0 
        right = 1

        if not nums:
            return 0
        
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right +=1
            
        return left + 1


solution = Solution()

nums1 = [1, 1, 2, 2, 3]
k1 = solution.removeDuplicates(nums1)
assert k1 == 3
assert nums1[:k1] == [1, 2, 3]

nums2 = [1, 1, 1]
k2 = solution.removeDuplicates(nums2)
assert k2 == 1
assert nums2[:k2] == [1]

nums3 = [1, 2, 3]
k3 = solution.removeDuplicates(nums3)
assert k3 == 3
assert nums3[:k3] == [1, 2, 3]

nums4 = []
k4 = solution.removeDuplicates(nums4)
assert k4 == 0
assert nums4[:k4] == []

print("Todos os testes passaram!")