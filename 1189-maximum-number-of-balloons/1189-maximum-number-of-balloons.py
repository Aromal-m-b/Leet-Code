class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = {}
        hmap['b'] = 0
        hmap['a'] = 0
        hmap['l'] = 0
        hmap['o'] = 0
        hmap['n'] = 0

        for character in text:
            if character in hmap:
                hmap[character] += 1
            else:
                continue

        rep = min(hmap['o']//2,hmap['l']//2)
        instance = min(rep,hmap['b'])
        instance = min(instance,hmap['a'])
        return min(instance,hmap['n'])
