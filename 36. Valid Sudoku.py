class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = collections.defaultdict(set)
        column = collections.defaultdict(set)
        sub_grid = collections.defaultdict(set)
    
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                if (board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in sub_grid[(i//3,j//3)]):
                    return False
                    
                row[i].add(board[i][j])
                column[j].add(board[i][j])
                sub_grid[(i//3,j//3)].add(board[i][j])
        
        return True
