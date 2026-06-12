class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        tree = {}
        for edge in edges:
            if edge[0] not in tree:
                tree[edge[0]] = []
            if edge[1] not in tree:
                tree[edge[1]] = []
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        print(tree)
    
        dp = {}

        def depth(node:int,parent:int) -> int:
            max_depth = 0
            for child in tree[node]:
                if child == parent:
                    continue
                max_depth = max(depth(child,node)+ 1,max_depth)
            return max_depth
        d = depth(1,-1)
        return ((2**(d-1)) % ((10**9)+7))