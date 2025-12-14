class Solution:
    def numberOfWays(self, corridor: str) -> int:
        adj = c = s = res = 0
        data = []
        if corridor.count('S')%2 != 0 or corridor.count('S') == 0:
            return 0
        elif corridor.count('S') == 2:
            return 1
        else:
            for i,value in enumerate(corridor):
                if value == "S":
                    c+=1
                    s = i+s
                if c == 2:
                    data.append([s-i,i])
                    c = s = 0
            res = 1
            for i in range(0,len(data)-1):
                start = data[i][1] + 1
                end = data[i+1][0]
                res = (len(corridor[start:end])+1) * res
        return int(res%(10**9+7))