class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for i in range(num1,num2+1):
            s = str(i)
            if len(s) >2:
                i= 2
                while i < len(s):
                    mid = int(s[i-1])
                    left = int(s[i-2])
                    right = int(s[i])
                    i+=1
                    if (mid > left and mid > right) or (mid < right and mid < left):
                        res += 1
        return res
            