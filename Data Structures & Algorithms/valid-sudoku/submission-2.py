class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            #1: row check
            freq={}
            for num in board[i]:
                if freq.get(num,0)==1:
                    return False
                if num!='.':
                    freq[num]=1
            #2: column check
            freq={}
            for row in board:
                if freq.get(row[i],0)==1:
                    return False
                if row[i]!='.':
                    freq[row[i]]=1
            #3: sub-box check
            freq={}
            row_start=(i//3)*3
            col_start=(i%3)*3
            for r in range(row_start,row_start+3):
                for c in range(col_start,col_start+3):
                    if freq.get(board[r][c],0)==1:
                        return False
                    if board[r][c]!='.':
                        freq[board[r][c]]=1
        return True


        