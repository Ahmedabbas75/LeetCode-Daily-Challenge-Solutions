class Solution:
    def climbStairs(self, n: int) -> int:
        stap1, step2 = 0, 1

        while n :
            stap1, step2 = step2, stap1 + step2
            n-= 1

        return step2

 