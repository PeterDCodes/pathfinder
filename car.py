class Car():

    def __init__(self, state=None, x=None, y=None):
        self.state = state
        self.x = x
        self.y = y


    def fire_check(state, x, y):
        #determine if on a fire
        tile = state[x][y]
        if tile == 'F':
            return True

    def find_moves(state, x, y):
        #determine the current moves
        moves = []
        tile = state[x][y]
        print(tile)