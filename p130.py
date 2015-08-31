class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == []: return 
        if len(board) <= 2: return 
        if len(board[0]) <= 2:  return 
        col = len(board) #|
        row = len(board[0]) #-
        for i in xrange(0, row):
            if board[0][i] == 'O':
                self.traversal(board, 0, i, 'O', 'T')
            if board[-1][i] == 'O':
                self.traversal(board, col-1, i, 'O', 'T')
        for i in xrange(0, col):
            if board[i][0] == 'O':
                self.traversal(board, i, 0, 'O', 'T')
            if board[i][-1] == 'O':
                self.traversal(board, i, row - 1, 'O', 'T')
        print board
        for rows in board:
            for i in xrange(0, len(rows)):
                if rows[i] == 'O':
                    rows[i] = 'X'
        for i in xrange(0, row):
            if board[0][i] == 'T':
                self.traversal(board, 0, i, 'T', 'O')
            if board[-1][i] == 'T':
                self.traversal(board, col-1, i, 'T', 'O')
        for i in xrange(0, col):
            if board[i][0] == 'T':
                self.traversal(board, i, 0, 'T', 'O')
            if board[i][-1] == 'T':
                self.traversal(board, i, row - 1, 'T', 'O') 
        return 
    def traversal(self, board, x, y, source, target):
        board[x][y] = target
        if x + 1 < len(board) and board[x+1][y] == source:
            self.traversal(board, x+1, y, source, target)
        if x - 1 > 0 and board[x-1][y] == source:
            self.traversal(board, x-1, y, source, target)
        if y + 1 < len(board[0]) and board[x][y+1] == source:
            self.traversal(board, x, y+1, source, target)
        if y - 1 > 0 and board[x][y-1] == source:
            self.traversal(board, x, y-1, source, target)
so = Solution()
l = [['X' for i in xrange(0, 3)] for j in xrange(0,3)]
l[1][1] = 'O'
print so.solve(l)