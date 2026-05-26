class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        else:
            res = 0
            cnt = 1
            print(nums)
            for i in range(1,len(nums)):
                if nums[i-1]+1 == nums[i] :
                    cnt += 1
                    print(cnt)
                else:
                    res = max(cnt,res)
                    cnt = 1
        return max(res,cnt)