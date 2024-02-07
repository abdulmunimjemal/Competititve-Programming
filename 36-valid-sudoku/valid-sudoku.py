class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        for i in range(9):
            row = set()
            column  = set()

            # traverse the whole row
            for j in range(9):
                val = board[i][j]
                if val in row and val != '.': return False
                row.add(val)
            
            # traverse the column corresponding to current row

            for j in range(9):
                val = board[j][i]
                if val in column and val != '.': return False
                column.add(val)
    
        # check 3 by 3 grid
        for j in range(0,9,3):
            for i in range(0,9,3):
                unique = set()
                for k in range(i,i+3):
                    for l in range(j, j+3):
                        val = board[k][l]
                        if val in unique and val != '.': return False
                        unique.add(val)
                
        return True
                    








        # check all columns

        # check 3 by 3 box
        