import unittest
from game import Game

class GameMethods(unittest.TestCase):

    def test_check_rows_X_in_row_0(self):
        myBoard = [['X','X','X'],['_','_','_'],['_','_','_']]
        game = Game(myBoard)
        self.assertEqual(game.check_rows(), 1)

    def test_check_rows_O_in_row_2(self):
        myBoard = [['_','_','_'],['_','_','_'],['O','O','O']]
        game = Game(myBoard)
        self.assertEqual(game.check_rows(), 2)

    def test_check_rows_no_winner(self):
        myBoard = [['_','_','O'],['X','_','_'],['X','O','O']]
        game = Game(myBoard)
        self.assertEqual(game.check_rows(), 0)

    def test_check_cols_X_in_cols_0(self):
        myBoard = [['X','_','_'],['X','_','_'],['X','_','_']]
        game = Game(myBoard)
        self.assertEqual(game.check_cols(), 1)

    def test_check_cols_0_in_cols_2(self):
        myBoard = [['_','_','O'],['_','_','O'],['_','_','O']]
        game = Game(myBoard)
        self.assertEqual(game.check_cols(), 2)

    def test_check_diags_X_in_neg_diag(self):
        myBoard = [['X','_','_'],['_','X','_'],['_','_','X']]
        game = Game(myBoard)
        self.assertEqual(game.check_diags(), 1)

    def test_check_diags_0_in_pos_diag(self):
        myBoard = [['_','_','O'],['_','O','_'],['O','_','_']]
        game = Game(myBoard)
        self.assertEqual(game.check_diags(), 2)

    def test_check_diags_no_winner(self):
        myBoard = [['O','_','X'],['_','O','_'],['O','X','_']]
        game = Game(myBoard)
        self.assertEqual(game.check_diags(), 0)

    def test_has_winner_X(self):
        myBoard = [['X','X','X'],['_','_','_'],['_','_','_']]
        game = Game(myBoard)
        self.assertEqual(game.has_winner(), 1)

    def test_has_winner_O(self):
        myBoard= [['O','O','O'],['_','_','_'],['_','_','_']]
        game = Game(myBoard)
        self.assertEqual(game.has_winner(), 2)

    def test_has_winner_None(self):
        myBoard = [['X','O','X'],['O','X','_'],['_','_','_']]
        game = Game(myBoard)
        self.assertEqual(game.has_winner(), 0)

    def test_check_valid_move_valid(self):
        myBoard = [['_','_','_'],['_','_','_'],['_','_','_']]
        game = Game(myBoard)
        self.assertTrue(game.check_valid_move([1,1,'X']))

    def test_check_valid_move_invalid(self):
        board = [['X','X','X'],['X','X','X'],['X','X','X']]
        game = Game(board)
        self.assertFalse(game.check_valid_move([1,1,'X']))
    
if __name__ == '__main__':
    unittest.main()