class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddsum = n*n
        evensum = n*(n+1)
        return self.gcd(oddsum,evensum)
    def gcd(self,a : int, b : int) -> int:
        temp = 0
        if a<b:
            temp = a
            a =b
            b = temp
        while(a%b != 0):
            temp = b
            b = a%b
            a = temp
        return b