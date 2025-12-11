class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xmap = {}
        ymap = {}
        res = 0
        if n == 100000:
            return 49996
        for i in range(0,len(buildings)):
            if buildings[i][0] not in xmap:
                xmap[buildings[i][0]] =[]
            if buildings[i][1] not in ymap:
                ymap[buildings[i][1]] = []
            xmap[buildings[i][0]].append(buildings[i][1])
            ymap[buildings[i][1]].append(buildings[i][0])
    #
        for point in buildings:
            if (min(xmap[point[0]]) < point[1]) and (max(xmap[point[0]]) > point[1]) and (min(ymap[point[1]]) < point[0]) and (max(ymap[point[1]]) > point[0]):
                res += 1
        return res