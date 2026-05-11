class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        rev = []
        for n in nums:
            while n>0:
                rev.append(n%10)
                n = n // 10
            temp = rev[::-1]
            for t in temp:
                res.append(t)
            rev = []
        return res