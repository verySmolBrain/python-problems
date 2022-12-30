class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, q = 0, deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,  j))
        
        time = 0
        while q and fresh > 0:
            time += 1

            for _ in range(len(q)):
                i, j = q.popleft()
                
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    xx, yy = i + dx, j + dy

                    if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]) and grid[xx][yy] == 1:
                        fresh -= 1
                        grid[xx][yy] = 2
                        q.append((xx, yy))
        
        return time if fresh == 0 else -1
        