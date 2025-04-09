
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == (str(x)[::-1])

sol = Solution()

print(sol.isPalindrome(123))
print(sol.isPalindrome(121))
print(sol.isPalindrome(-123))