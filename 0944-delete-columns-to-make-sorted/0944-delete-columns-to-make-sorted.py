class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        hmap = {}
        count = 0
        for value in strs:
            for i,ch in enumerate(value):
                if i not in hmap:
                    hmap[i] = []
                hmap[i].append(ch)
        for i in hmap:
            if hmap[i] != sorted(hmap[i]):
                count+=1 
        return count
