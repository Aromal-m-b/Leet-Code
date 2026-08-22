class Solution:
    def checkDivisibility(self, n: int) -> bool:
        add = int(str(n)[0])
        mul = int(str(n)[0])
        temp = str(n)
        for i in range(1,len(temp)):
            add += int(temp[i])
            mul *= int(temp[i])
        temp = int(n/(mul+add))
        if temp*(mul+add) == n:
            return True
        else:
            return False 