class Solution:
    def climbStairs(self, n: int) -> int:
        val_map = {}
        res = 0
        def helper(x:int,map:dict):
            if x in val_map:
                return val_map[x]
            else:
                if x == 1:
                    val_map[x] = 1
                    return 1
                elif x == 2:
                    val_map[x] = 2
                    return 2
                else:
                    val_map[x] = helper(x-1,val_map) + helper(x-2,val_map)
                    return val_map[x] 
        res = helper(n,val_map)
        return res