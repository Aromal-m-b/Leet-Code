class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base = max(nums)
        if nums.count(base) != 2:
            return False
        return all((nums.count(n)==1 )for n in range (1,base))
         
