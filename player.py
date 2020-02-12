

class Player:
    def __init__(self, name):
        self.name = name

    # get input
    def get_move(self):
        col, row, player = input("Enter a two value: ").split() 
        int(col)
        int(row)
        return [int(col),int(row),player]


