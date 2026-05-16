class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        #horizontal check
        for i in range(len(board)):
            seen.clear()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        #column check
        for j in range(len(board[0])):
            seen.clear()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        # sub-boxes check
        for square in range(9):
            seen.clear()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True