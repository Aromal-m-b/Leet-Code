class Solution:
    def good(self,num):
        valid = [2,5,6,9]
        invalid = [3,4,7]
        norm = [1,0,8]
        flag = 0
        l = 0
        stat = "checking"
        while num > 0:
            l += 1
            temp = num%10
            num = num//10
            if temp in valid:
                stat = "valid"
                continue
            elif temp in invalid:
                stat = "invalid"
                break
            elif temp in norm:
                flag += 1
            
        if flag == l:
            stat = "invalid"
        return stat == "valid"
                
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(1,n+1):
            if self.good(i):
                res += 1
        return res
            
            