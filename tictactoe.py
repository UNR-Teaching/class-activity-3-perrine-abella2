""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""


class Board(object):

    board = [['_','_','_'],['_','_','_'],['_','_','_']]

    def __init__(self):
        self.board = [['_','_','_'],['_','_','_'],['_','_','_']]

    def print_board(self):    
        print (self.board[0][0] + " " + self.board[0][1] + " " + self.board[0][2])
        print (self.board[1][0] + " " + self.board[1][1] + " " + self.board[1][2])
        print (self.board[2][0] + " " + self.board[2][1] + " " + self.board[2][2])
        return self.board

    def check_full(self):
        for i in range(0,2):
            for j in range(0,2):
                if self.board[i][j] == '_':
                    return False
        return True

    def check_empty(self):
        for i in range(0,2):
            for j in range(0,2):
                if self.board[i][j] != '_':
                    return False
        return True

    def mark_square(self, column, row, player):
        self.board[row][column] = player
        return self.board
   
