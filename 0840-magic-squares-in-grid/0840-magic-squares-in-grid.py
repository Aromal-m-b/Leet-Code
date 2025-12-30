class Solution:
    def numMagicSquaresInside(self,grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        flag = 1
        res = 0
        result = {}
        nums = set()
        for i in range (0,row-2):
            for j in range(0,column-2):
                flag = 1
                if grid[i][j] < 10 and grid[i][j] > 0:
                    nums.add(grid[i][j])
                if grid[i][j+1] < 10 and grid[i][j+1] > 0:
                    nums.add(grid[i][j+1])
                if grid[i][j+2] < 10 and grid[i][j+2] > 0:
                    nums.add(grid[i][j+2])
                if grid[i+1][j] < 10 and grid[i+1][j] > 0:
                    nums.add(grid[i+1][j])
                if grid[i+1][j+1] < 10 and grid[i+1][j+1] > 0:
                    nums.add(grid[i+1][j+1])
                if grid[i+1][j+2] < 10 and grid[i+1][j+2] > 0:
                    nums.add(grid[i+1][j+2])
                if grid[i+2][j] < 10 and grid[i+2][j] > 0:
                    nums.add(grid[i+2][j])
                if grid[i+2][j+1] < 10 and grid[i+2][j+1] > 0:
                    nums.add(grid[i+2][j+1])
                if grid[i+2][j+2] < 10 and grid[i+2][j+2] > 0:
                    nums.add(grid[i+2][j+2])
                if len(nums) != 9:
                    flag = 0
                nums = set()
                sum = grid[i][j]+grid[i][j+1]+grid[i][j+2]
                if sum != grid[i+1][j]+grid[i+1][j+1]+grid[i+1][j+2]:
                    flag = 0
                if sum != grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]:
                    flag = 0
                if sum != grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]:
                    flag = 0
                if sum != grid[i][j]+grid[i+1][j]+grid[i+2][j]:
                    flag = 0
                if sum != grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]:
                    flag = 0
                if sum != grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]:
                    flag=0
                if sum != grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]:
                    flag = 0
                if flag == 1:
                    res+=1
        return res
        