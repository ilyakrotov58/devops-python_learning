
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == (str(x)[::-1]):
            return True
        else:
            return False

sol = Solution()

print(sol.isPalindrome(123))
print(sol.isPalindrome(121))
print(sol.isPalindrome(-123))