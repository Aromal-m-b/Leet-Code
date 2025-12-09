class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        rhmap = {}
        count = 0
        mod = 10**9+7
        for n in nums:
            if n in rhmap:
                rhmap[n]+=1
            else:
                rhmap[n] = 1
        lhmap = dict.fromkeys(rhmap.keys(),0)
        for i in range(0,len(nums)):
            num = nums[i]
            rhmap[num] -=1
            k = num*2
            if k in lhmap:
                if k in rhmap:
                    count = rhmap[k]*lhmap[k] + count
            lhmap[num] += 1
        return count%mod

