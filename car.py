class Car():

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return(f'Car Position:({self.x},{self.y})')

    def find_moves(board, x, y):
        #determine the current moves
        moves = []
        tile = board[x][y]
        print(tile)

