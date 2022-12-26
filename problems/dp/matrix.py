class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = math.inf
                    if i > 0:
                        mat[i][j] = min(mat[i-1][j] + 1, mat[i][j])
                    if j > 0:
                        mat[i][j] = min(mat[i][j-1] + 1, mat[i][j])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] != 0:
                    if i + 1 < m:
                        mat[i][j] = min(mat[i+1][j] + 1, mat[i][j])                    
                    if j + 1< n:
                        mat[i][j] = min(mat[i][j+1] + 1, mat[i][j])                    
        return mat