from tictactoe import Board
from player import Player

class Game:

    def __init__(self, board):
        self.Board = board

    def check_rows(self):
        for i in range(2):
            if self.Board.board[i][0] == self.Board.board[i][1] == self.Board.board[i][2]:
                if self.Board.board[i][0] == 'X':
                    return 1
                else:
                    return 2
        return 0 

    def check_cols(self):
        for i in range(2):
            if self.Board.board[0][i] == self.Board.board[1][i] == self.Board.board[2][i]:
                if self.Board.board[0][i] == 'X':
                    return 1
                else:
                    return 2
        return 0 

    def check_diags(self):
        if self.Board.board[0][0] == self.Board.board[1][1] == self.Board.board[2][2]:
            if self.Board.board[0][0] == 'X':
                return 1
            else:
                return 2 
        elif self.Board.board[0][2] == self.Board.board[1][1] == self.Board.board[2][0]:       
            if self.Board.board[0][2] == 'X':
                return 1
            else:
                return 2 
        else:
            return 0

    # 
    def has_winner(self):
        rows = self.check_rows()
        cols = self.check_cols()
        diags = self.check_diags()

        if rows != 0:
            return rows
        elif cols != 0:
            return cols 
        elif diags != 0:
            return diags
        else:
            return 0

    def check_valid_move(self, input_list):
        row = input_list[1]
        col = input_list[0]
        if self.Board.board[row][col] == '_':
            return True
        else:
            return False

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        - play while there is no winner
        - ask for input from player 1
            - keep asking while not a valid input
        - ask for input from player 2
            - keep asking while not valid input
        check for winner and check if board is full
        
        :return: (str) the letter representing the player who won
        """
        player1 = Player(player1, 'X')
        player2 = Player(player2, 'O')
        winner = 0
        while winner == 0:
            input_list = player1.getmove()
            self.Board.board.mark_square(input_list[0], input_list[1], input_list[2])
            winner = self.has_winner()
            if winner != 0:
                break
            input_list = player2.getmove()
            self.Board.board.mark_square(input_list[0], input_list[1], input_list[2])
            winner = self.has_winner()
            
        
# if __name__ == '__main__':
#     board = Board()
#     winner = board.play_game()
#     print("{} has won!".format(winner))
