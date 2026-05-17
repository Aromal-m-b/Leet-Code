class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        res = True
        graph = {}
        def create_graph(graph,start,arr,res):
            graph[start] = []
            if start + arr[start] < len(arr) and start+arr[start] not in graph:
                if arr[start+arr[start]]  == 0:
                    return True
                graph[start].append(start+arr[start])
                res = create_graph(graph,start + arr[start],arr,res)
            if start - arr[start] >= 0 and start - arr[start] not in graph:
                if arr[start - arr[start]]  == 0:
                    return True
                graph[start].append(start-arr[start])
                res = create_graph(graph,start - arr[start],arr,res)
            return res
        if arr[start] == 0:
            return True
        else:
            return create_graph(graph,start,arr,False)
