class Solution:
    def countIslands(self,grid : list[list[int]] , k: int) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        is_island = 0
        island = 0
        def boundary(l : int,w : int,node : list[int],visited : list[list[int]],size : int,grid : list[list[int]]) -> tuple[list[list[int]],int]:
            if node[0]+1 < l:
                if visited[node[0] + 1][node[1]] == 0 and grid[node[0] + 1][node[1]] != 0:
                    visited[node[0] + 1][node[1]] = 1
                    size += grid[node[0] +1][node[1]]
                    visited ,size= boundary(l,w,[node[0] + 1,node[1]],visited,size,grid)
            if node[0] - 1 >= 0:
                if visited[node[0] - 1][node[1]] == 0 and grid[node[0] - 1][node[1]] != 0:
                    visited[node[0] - 1][node[1]] = 1
                    size += grid[node[0] - 1][node[1]]
                    visited ,size= boundary(l, w, [node[0] - 1,node[1]], visited,size,grid)
            if node[1] + 1< w:
                if visited[node[0]][node[1]+1] == 0 and grid[node[0]][node[1]+1] != 0:
                    visited[ node[0] ][node[1] + 1 ] = 1
                    size += grid[node[0]][node[1] + 1]
                    visited ,size= boundary(l, w, [node[0],node[1]+1], visited,size,grid)
            if node[1] - 1 >= 0:
                if visited[node[0]][node[1]-1] == 0 and grid[node[0]][node[1]-1] != 0:
                    visited[ node[0] ][ node[1] - 1 ] = 1
                    size += grid[ node[0] ][ node[1] - 1 ]
                    visited ,size= boundary(l, w, [node[0],node[1]-1], visited,size,grid)
            return visited,size
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and visited[i][j] == 0:
                    size = grid[i][j]
                    visited[i][j] = 1
                    visited,size = boundary(len(grid),len(grid[0]),[i,j],visited,size,grid)
                    if size%k == 0 :
                        count += 1
        return count
        