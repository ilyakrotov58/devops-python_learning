from typing import List, Optional

#Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

#You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[list[int]]:
        for i in range(len(nums)):
            for y in range(i + 1, len(nums)):
                if nums[i] + nums[y] == target:
                    return[i, y]


sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))