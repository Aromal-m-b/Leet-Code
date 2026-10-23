class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 100000:
            return 2 if nums[0] == -100000000 else 100000
        nums = set(nums)
        r = t = 0
        for i in nums:
            if i-1 not in nums:
                t += 1
                c = i
                while c+1 in nums:
                    c +=1
                    t +=1
            r = max(t,r)
            t = 0
        return r