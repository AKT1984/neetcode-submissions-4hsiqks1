class Solution:
    def climbStairs(self, n: int) -> int:
        val1 = 1
        val2 = 1
        for _ in range(n):
            temp = val2
            val2 += val1
            val1 = temp

        return val1