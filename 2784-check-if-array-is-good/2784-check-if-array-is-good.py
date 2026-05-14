class Solution:
    def isGood(self, nums: List[int]) -> bool:
        flag = 0
        nums.sort()
        print(nums)
        if nums[-1] == len(nums)-1:
            for i in range(0,len(nums)-1):
                if nums[i] == i+1:
                    flag = 0
                else:
                    flag = 1
                    break
            if flag == 0:
                return True
            else:
                return False
        else:
            return False
