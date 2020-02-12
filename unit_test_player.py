import unittest
from player import Player

class PlayerMethods(unittest.TestCase):

    def test_get_move(self):
        player1 = Player("player1")
        input_list = player1.get_move()
        #print(input_list)
        self.assertEqual([1,1,'X'], input_list)

if __name__ == '__main__':
    unittest.main()