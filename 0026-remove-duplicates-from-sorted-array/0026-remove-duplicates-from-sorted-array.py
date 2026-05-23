class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = [nums[0]]
        cnt = 1
        for i in range(1,len(nums)):
            if res[-1] != nums[i]:
                res.append(nums[i])
                cnt+=1
        nums[:] = res
        return cnt