class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for key,v in count.items():
            bucket[v].append(key)
        r = []
        for f in range(len(nums),0,-1):
            for v in bucket[f]:
                r.append(v)
                if len(r) == k:
                    return r
        return r