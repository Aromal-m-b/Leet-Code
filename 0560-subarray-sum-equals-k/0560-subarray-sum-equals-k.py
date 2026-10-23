class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0] = 1
        s = 0
        r = 0
        for i in nums:
            s += i
            r += hmap[s-k]
            hmap[s] += 1
        return r