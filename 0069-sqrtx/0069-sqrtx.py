class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        low = 1
        high = x-1
        while high >= low:
            mid = (high+low)//2
            res = mid * mid
            if res == x:
                return mid
            elif res > x:
                high = mid - 1
            elif res < x:
                low = mid + 1
        return high
