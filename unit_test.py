import unittest
from tictactoe import Board

class TestTicTacToeMethods(unittest.TestCase):

    def test_print_board(self):
        board = Board()
        expected = [['_','_','_'],['_','_','_'],['_','_','_']]
        self.assertEqual(board.print_board(), expected)

    def test_mark_square_X_in_0_0(self):
        board = Board()
        expected = [['X','_','_'],['_','_','_'],['_','_','_']]
        self.assertEqual(board.mark_square(0,0,"X"), expected)

    def test_mark_square_O_in_0_0(self):
        board = Board()
        expected = [['O','_','_'],['_','_','_'],['_','_','_']]
        self.assertEqual(board.mark_square(0,0,"O"), expected)

    def test_mark_square_X_in_1_1(self):
        board = Board()
        expected = [['_','_','_'],['_','X','_'],['_','_','_']]
        self.assertEqual(board.mark_square(1,1,"X"), expected)

    def test_mark_square_O_in_1_1(self):
        board = Board()
        expected = [['_','_','_'],['_','O','_'],['_','_','_']]
        self.assertEqual(board.mark_square(1,1,"O"), expected)

    def test_mark_square_X_in_2_2(self):
        board = Board()
        expected = [['_','_','_'],['_','_','_'],['_','_','X']]
        self.assertEqual(board.mark_square(2,2,"X"), expected)

    def test_mark_square_O_in_2_2(self):
        board = Board()
        expected = [['_','_','_'],['_','_','_'],['_','_','O']]
        self.assertEqual(board.mark_square(2,2,"O"), expected)

    def test_check_full_no(self):
        board = Board()
        self.assertFalse(board.check_full())
    
    def test_check_full_no(self):
        board = Board()
        board.board = [['X','X','X'],['X','X','X'],['X','X','X']]
        self.assertTrue(board.check_full())

if __name__ == '__main__':
    unittest.main()
