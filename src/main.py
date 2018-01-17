from c4 import Board, InvalidMove

class Game(object):
    """

    """
    def __init__(self):
        self.player_turn = 1
        self.board = Board()

    def play(self):
        """

        :return:
        """
        while self.board.check_win() is None:
            print(self.board)
            self.player_turn = (self.player_turn + 1) % 2
            while True:
                print('Player {}, choose column for move:'.format(self.player_turn))
                col = raw_input()

                if col == 'q':
                    print('Quitting')
                    return

                try:
                    col_int = int(col)
                except ValueError:
                    print('That is not a number')
                    continue

                try:
                    self.board.add_disc(col_int, self.player_turn)
                    break
                except InvalidMove:
                    print('That is not a valid move')
                    continue

        else:
            print('Winner is {}'.format(self.player_turn))



quit = False
in_game = False

while not quit:
    if not in_game:
        print('Press enter to start game, q to exit')
        inp = raw_input()
        if inp == 'q':
            print('Exiting')
            break
        game = Game()
        in_game = True
    else:
        game.play()
        in_game = False
