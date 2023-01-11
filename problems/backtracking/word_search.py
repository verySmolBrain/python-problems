class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, i, j, word, 0):
                    return True 
        
        return False
    
    def search(self, board, row, col, word, i):
        if len(word) == i:
            return True 
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False 
        if board[row][col] != word[i]:
            return False 
        
        char = board[row][col]
        board[row][col] = " "
        
        res = \
        self.search(board, row + 1, col, word, i + 1) or \
        self.search(board, row - 1, col, word, i + 1) or \
        self.search(board, row, col + 1, word, i + 1) or \
        self.search(board, row, col - 1, word, i + 1)
        
        board[row][col] = char 
        return res
        