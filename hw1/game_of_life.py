class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        res_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                nbrs = 0
                shifts = ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 1))
                for i_shift, j_shift in shifts:
                    new_i = i + i_shift
                    new_j = j + j_shift
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and board[new_i][new_j] == 1:
                        nbrs += 1
                if board[i][j] == 1 and nbrs in [2, 3] or board[i][j] == 0 and nbrs == 3:
                    res_board[i][j] = 1
                else:
                    res_board[i][j] = 0
        for i in range(len(res_board)):
            board[i] = res_board[i]
        return
