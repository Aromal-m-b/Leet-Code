class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        print(ord('a'))
        for char_s, char_t in zip(s,t):
            count[ord(char_s) - 97] += 1
            count[ord(char_t) - 97] -= 1
        return all(c==0 for c in count)