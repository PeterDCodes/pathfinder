from car import Car

board_size = 10

def main():

    state = [['x'for _ in range(board_size)] for _ in range(board_size)]

    car = Car(state=state)

    for row in car.state:
        print(row)

    #recieve the starting x location of the car
    while True:
        startx = input('X: ')
        try:
            startx = int(startx)
            if startx <= board_size and startx >= 1:
                car.x = startx
                break
        except ValueError:
            print("Must enver valid integer")
    
    #recieve the starting x location of the car
    while True:
        starty = input('Y: ')
        try:
            starty = int(starty)
            if starty <= board_size and starty >= 0:
                car.y=starty
                break
        except ValueError:
            print("Must enver valid integer")

    print(car)

    #recieve the location of a fire

main()
