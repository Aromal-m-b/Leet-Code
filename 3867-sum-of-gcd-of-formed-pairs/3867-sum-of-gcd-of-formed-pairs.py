class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        largest = nums[0]
        prefixgcd = []
        i=0
        for i in range(len(nums)):
            largest = max(largest,nums[i])
            prefix = self.gcd(largest,nums[i])
            prefixgcd.append(prefix)
        prefixgcd.sort()
        i = 0
        res = 0
        count = 0
        while (i < len(prefixgcd)//2):
            first = prefixgcd[i]
            second = prefixgcd[len(prefixgcd)-i-1]
            res += self.gcd(first,second)
            count+=2
            i+=1
        return res

    def gcd(self,a : int,b : int):
        temp =0 
        if a < b:
            temp = a
            a = b
            b = temp
        while (b != 0):
            a , b = b, a%b
        return a