# You are given a string s.
# The score of a string is defined as the sum of
# the absolute difference between the ASCII values of adjacent characters.

# Return the score of s.

class Solution:
    def scoreOfString(self, s: str) -> int:
        numbers = []
        for letter in s:
            numbers.append(ord(letter))
        last_diff = 0
        last_num = 0
        for i in range(len(numbers) - 1):
            if i == 0:
                last_num = numbers[0]
            current_diff = last_num - numbers[i + 1]
            last_diff = last_diff + abs(current_diff)
            last_num = numbers[i + 1]
        return last_diff

sol = Solution()
print(sol.scoreOfString("zaz"))