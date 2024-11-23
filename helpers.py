
#function to print the game board for user to see
def print_board(board):
        for row in board:
            print(row)


def start_fire(board):
    #recieve a location of the fire and add it to the board
    # a fire can not be started unless the space is 'empty' aka. represented by an 'x'
    print("START FIRE")

    while True:
        #recieve the x location of the fire
        while True:
            x = input('FIRE X: ')
            try:
                x = int(x)
                if x <= len(board) and x >= 0:
                    fire_x = x
                    break
                    
            except ValueError:
                print('Must Enter Integer')

        #recieve the y location of the fire
        while True:
            y = input('FIRE Y: ')
            try:
                y = int(y)
                if y <= len(board) and y >= 0:
                    fire_y = y
                    break
                    
            except ValueError:
                print('Must Enter Integer')

        if board[fire_x][fire_y] == 'x':
            board[fire_x][fire_y] = 'F'
            print_board(board)
            break
        else:
            print("Fire can not be started at that location")
