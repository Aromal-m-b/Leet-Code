class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 2:
            return n
        else:
            one = 2
            two = 1
            ans = 0
            for i in range(3,n+1):
                ans = one + two
                two = one
                one = ans
            return ans