class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) != nums[len(nums)-1] + 1 or len(nums)-1 != nums[-1] or len(nums)-1 != nums[-2]:
            return False
        if len(nums) >= 3:
            for i in range(0,len(nums)-2):
                if nums[i] != i+1:
                    return False
        return True
         
