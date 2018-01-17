class InvalidMove(StandardError):
    pass


class Board(object):
    '''
    Connect  board
    '''

    NUM_COLS = 7
    NUM_ROWS = 6
    GLPYHS = {None: '.', 0: 'X', 1: 'O'}
    WIN_LENGTH = 4

    def __init__(self):
        self.board = [[] for _ in range(self.NUM_COLS)]

    def __str__(self):
        """
        A string representation of the board to print to a terminal
        :return:
        """
        rows = self._rows()
        row_strs = []
        for row in rows:
            row_strs.append(' '.join([self.GLPYHS[i] for i in row]))
        return '\n'.join(row_strs)

    def add_disc(self, col, player):
        """
        Add a disc to the board

        :param col: Column to add disc to
        :param player: player adding disc
        :return: None
        """
        if col > self.NUM_COLS - 1:
            raise InvalidMove('Column does not exist')

        if len(self.board[col]) < self.NUM_ROWS:
            self.board[col].append(player)
        else:
            raise InvalidMove('Column full')

    def _fill_board(self):
        """
        Fill each column with None up to NUM_ROWS
        :return: List of lists representing a full board
        """
        full_board = []
        for col in self.board:
            full_col = col + [None] * (self.NUM_ROWS - len(col))
            full_board.append(full_col)

        return full_board

    def _rows(self):
        """
        List of lists of board rows, starting from the top row
        :return:
        """
        full_board = self._fill_board()
        rows = []
        for i in reversed(range(self.NUM_ROWS)):
            rows.append([col[i] for col in full_board])
        return rows

    def _diagonals(self):
        return []

    def check_win(self):
        """
        Check to see whether either player has won.
        #TODO doesn't handle both players having winning sequences
        :return: None for no winner, 0/1 if either of those players wins.
        """
        cols = self._fill_board()
        rows = self._rows()
        diags = self._diagonals()

        for direction in [cols, rows, diags]:
            for line in direction:
                last_disc = None
                count = 0
                for disc in line:
                    if disc == last_disc:
                        count += 1
                    else:
                        last_disc = disc
                        count = 1
                    if count == self.WIN_LENGTH and disc is not None:
                        return disc
        else:
            return None


# board = Board()
# board.add_disc(0, 1)
# board.add_disc(1, 1)
# board.add_disc(2, 1)
# board.add_disc(3, 1)
# print(board)
# winner = board.check_win()
# print('Winner: {}'.format(winner))
