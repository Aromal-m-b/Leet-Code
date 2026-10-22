class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map = defaultdict(list)
        for i in strs:
            map["".join(sorted(i))].append(i)
        return list(map.values())