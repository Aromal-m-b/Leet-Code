class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        sum = 0
        for i in range(0,len(cost),3):
            sum += cost[i]
            if i+1 < len(cost):
                sum += cost[i+1]
        return sum