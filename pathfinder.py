from car import Car
from helpers import print_board, start_fire

board_size = 10

def main():

    board = [['x'for _ in range(board_size)] for _ in range(board_size)]

    car = Car()

    print("Pathfinder Game")
    print(car)

    #recieve the starting x location of the car
    print('Set Car Starting Position')
    while True:
        startx = input('X: ')
        try:
            startx = int(startx)
            if startx <= board_size and startx >= 1:
                car.x = startx
                break
            else:
                print('Car position located outside of board')
        except ValueError:
            print("Must enver valid integer")
    
    #recieve the starting y location of the car
    while True:
        starty = input('Y: ')
        try:
            starty = int(starty)
            if starty <= board_size and starty >= 0:
                car.y=starty
                break
            else:
                print('Car position located outside of board')
        except ValueError:
            print("Must enver valid integer")


    #update start position of the car on the board
    board[car.y][car.x] = 'C'

    print_board(board)


    #add fire to board
    start_fire(board)


    #fine the moves possible and select the best path to get to the fire
    


main()