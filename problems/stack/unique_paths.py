class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def findPaths(m, n, i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            
            downPath, rightPath = 0, 0
            if i + 1 < m:
                downPath = findPaths(m, n, i + 1, j)
            if j + 1 < n:
                rightPath = findPaths(m, n, i, j + 1)
            
            return downPath + rightPath
        
        return findPaths(m, n, 0, 0)

class Solution: # Memoization
    def uniquePaths(self, m: int, n: int) -> int:
        def findPaths(m, n, i, j, memo):
            if i == (m - 1) and j == (n - 1):
                return 1
            elif i > (m - 1) or j > (n - 1):
                return 0
            
            if memo[i][j] > 0:
                return memo[i][j]

            memo[i][j] = findPaths(m, n, i + 1, j, memo) + findPaths(m, n, i, j + 1, memo)
            return memo[i][j]
        
        memo = [[0 for _ in range(n)] for _ in range(m)]
        return findPaths(m, n, 0, 0, memo)