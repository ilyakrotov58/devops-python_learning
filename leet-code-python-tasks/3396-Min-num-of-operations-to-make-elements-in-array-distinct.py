from typing import List

# You are given an integer array nums.
# You need to ensure that the elements in the array are distinct.
# To achieve this, you can perform the following operation any number of times:
#
# Remove 3 elements from the beginning of the array.
# If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements.
# Return the minimum number of operations needed to make the elements in the array distinct.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0

        while True:
            if len(set(nums)) == len(nums): return result
            else:
                nums = nums[3:]
                result += 1

sol = Solution()
print(sol.minimumOperations([1,2,3,4,2,3,3,5,7]))
print(sol.minimumOperations([4,5,6,4,4]))
print(sol.minimumOperations([6,7,8,9]))