import collections

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        MOD = 10**9 + 7

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        queue = collections.deque([(1, 0)])  # (node, depth)
        visited = {1}
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            max_depth = depth

            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
        
        path_length = max_depth

        if path_length == 0:
            return 0
        
        # The number of ways to choose an odd number of edges from path_length
        # to assign a weight of 1 (which makes the total cost odd)
        # is 2^(path_length - 1).
        return pow(2, path_length - 1, MOD)