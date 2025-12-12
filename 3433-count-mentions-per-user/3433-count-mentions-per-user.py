import re
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        hmap = {}
        n= numberOfUsers
        for event in events:
            time = int(event[1])
            if time not in hmap:
                hmap[time] = []
            hmap[time].append([event[0],event[2]])
        hmap = dict(sorted(hmap.items()))
        for k, lst in hmap.items():
            offline = [entry for entry in lst if entry[0] == 'OFFLINE']
            others  = [entry for entry in lst if entry[0] != 'OFFLINE']
            hmap[k] = offline + others

        online = [1] * n
        offline = [[]]
        res = [0]*n
        i = 1



        for time,value in hmap.items():
            if sum(online) != n:
                for stamp in offline[1:]:
                    if time-stamp[0] >=60:
                        online[stamp[1]] = 1
                        offline.remove(stamp)
                        i-=1
            for entry in value: 
                if entry[0] == "MESSAGE":
                    query = entry[1].replace(" ","")
                    if query == "ALL":
                        res = [x + 1 for x in res]
                    elif query == "HERE":
                        res = [res[i] + online[i] for i in range(n)]
                    else:
                        cust = re.findall(r'id(\d+)', query, flags=re.IGNORECASE)
                        for j in cust:
                            res[int(j)] += 1
                elif entry[0] == "OFFLINE":
                    online[int(entry[1])] = 0
                    offline.append([time,int(entry[1])])
                    i+=1
        return res