class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for b_row in range(9):
            for b_col in range(9):
                if board[b_row][b_col] == ".":
                    continue
                if ((board[b_row][b_col] in rows[b_row]) or 
                (board[b_row][b_col] in cols[b_col]) or 
                (board[b_row][b_col] in square[(b_row // 3), (b_col // 3)])):
                    return False
                rows[b_row].add(board[b_row][b_col])
                cols[b_col].add(board[b_row][b_col])
                square[(b_row // 3), (b_col // 3)].add(board[b_row][b_col])
        
        return True
        