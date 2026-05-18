from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        queue = deque([0])
        visited = {0}
        hmap = {}
        for i in range(len(arr)):
            if arr[i] not in hmap:
                hmap[arr[i]] = []
            hmap[arr[i]].append(i)
        layer = 1 
        ret = 1
        if len(arr) == 1:
            return 0
        while queue:
            node = queue.popleft()
            if node + 1 < len(arr) and node+1 not in visited:
                queue.append(node+1)
                visited.add(node+1)
                if node + 1 == len(arr) - 1:
                    return ret
            if node - 1 >= 0 and node-1 not in visited:
                queue.append(node - 1)
                visited.add(node - 1)
            if arr[node] in hmap:
                res = hmap.pop(arr[node])
                for i in res:
                    if i != node and i not in visited:
                        queue.append(i)
                        visited.add(i)
                        if i == len(arr) - 1:
                            return ret
            layer -= 1
            if layer == 0:
                layer = len(queue)
                ret = ret +  1

            