import unittest
from player import Player
from tictactoe import Board
from game import Game

class PlayGameMethods(unittest.TestCase):

    def test_game_creates_board(self):
        board = Board()
        game = Game(board)
        self.assertTrue(game.Board.check_empty())

    def test_game_mark_moves_no_inputs(self):
        board = Board()
        game = Game(board)
        game.Board.mark_square(1,1,'X')
        game.Board.mark_square(0,0,'O')
        game.Board.mark_square(2,2,'X')
        game.Board.mark_square(0,1,'O')
        game.Board.mark_square(1,2,'X')
        game.Board.mark_square(2,1,'O')
        game.Board.mark_square(0,2,'X')
        game.Board.print_board()
        expected = [['O','_','_'],['O','X','O'],['X','X','X']]
        self.assertEqual(game.Board.board, expected)

    def test_game_checks_board_for_winner_none(self):
        board = Board()
        game = Game(board)
        game.Board.mark_square(1,1,'X')
        game.Board.mark_square(2,1,'O')
        game.Board.mark_square(0,0,'X')
        game.Board.mark_square(2,2,'O')
        self.assertEqual(0, game.has_winner())

    def test_game_checks_board_for_winner_row_X(self):
        board = Board()
        game = Game(board)
        game.Board.mark_square(0,0,'X')
        game.Board.mark_square(0,1,'X')
        game.Board.mark_square(0,2,'X')
        self.assertEqual(1, game.has_winner())

if __name__ == '__main__':
    unittest.main()