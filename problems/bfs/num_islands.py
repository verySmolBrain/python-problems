class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    self.coverIsland(grid, i, j)
        
        return num_islands
    
    def coverIsland(self, grid, r, c):
        q = deque([(r, c)])

        while q:
            i, j = q.pop()

            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '#'
                q.extend([(i - 1, j), (i + 1,  j), (i, j - 1), (i, j + 1)])