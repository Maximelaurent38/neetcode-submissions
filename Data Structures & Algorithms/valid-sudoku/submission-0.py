class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for i in range(n):
            ligne = board[i]
            seen = []
            for l in ligne:
                if l != ".":
                    if l in seen:
                        return False
                    else:
                        seen.append(l)

        for k in range(n):
            colonne = [board[j][k] for j in range(n)]
            seen = []
            for l in colonne:
                if l != ".":
                    if l in seen:
                        return False
                    else:
                        seen.append(l)
        
        for square in range(n):
            seen = []
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i
                    col = (square%3)*3 +j
                    if board[row][col] != ".":
                        if board[row][col] in seen:
                            return False
                        seen.append(board[row][col])
        
        return True
            
        