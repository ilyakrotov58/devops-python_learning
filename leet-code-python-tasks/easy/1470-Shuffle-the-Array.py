from typing import List

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [item for pair in zip(nums[:n], nums[n:]) for item in pair]


sol = Solution()
print(sol.shuffle([2,5,1,3,4,7], 3))
print(sol.shuffle([1,2,3,4,4,3,2,1], 4))
print(sol.shuffle([1,1,2,2], 2))