# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have.
# Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        jewels_set = set(jewels)
        for i in stones:
            if i in jewels_set:
                result += 1
        return result

sol = Solution()

print(sol.numJewelsInStones("Aa", "aAAert"))
print(sol.numJewelsInStones("s", "SSS"))