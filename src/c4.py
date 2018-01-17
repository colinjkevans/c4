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
        full_board = self._fill_board()
        row_strs = []
        for i in reversed(range(self.NUM_ROWS)):
            row_strs.append(' '.join([self.GLPYHS[col[i]] for col in full_board]))

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

    def check_win(self):
        """
        Check to see whether either player has won.
        #TODO doesn't handle both players having winning sequences
        :return: None for no winner, 0/1 if either of those players wins.
        """
        full_board = self._fill_board()
        return self._check_columns(full_board)

    def _check_rows(self):
        pass

    def _check_columns(self, full_board):
        last_disc = None
        count = 0
        for col in full_board:
            for disc in col:
                if disc is None:
                    # Iterating up the column, so any empty space found means
                    # all above will be empty too
                    break
                elif disc == last_disc:
                    count += 1
                else:
                    last_disc = disc
                    count = 1

                if count == self.WIN_LENGTH:
                    return disc
        else:
            return None

    def _check_diagonals(self):
        pass


board = Board()
board.add_disc(0,0)
board.add_disc(0,0)
board.add_disc(0,0)
board.add_disc(0,0)
print(board)
winner = board.check_win()
print('Winner: {}'.format(winner))
