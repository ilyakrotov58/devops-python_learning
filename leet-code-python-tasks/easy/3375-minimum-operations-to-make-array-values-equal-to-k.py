from typing import List

# Return the number of distinct integers in the array that are greater than k

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = len(set([num for num in nums if num > k]))
        return result if result > 0 else -1

sol = Solution()
print(sol.minOperations([1], 1))
print(sol.minOperations([5,2,5,4,5], 2))
print(sol.minOperations([2,1,2], 2))
print(sol.minOperations([9,7,5,3], 1))