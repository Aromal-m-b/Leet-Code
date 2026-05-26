class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hmap = {}
        nums = set(word)
        cnt = 0
        for n in nums:
            if n not in hmap:
                hmap[n] = 0
            if (n.lower() in hmap) and (n.upper() in hmap):
                cnt+=1
        print(hmap)
        return cnt

