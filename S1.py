position = 1
while True:
    move = int(input())
    if move == 0:
        print("You Quit!")
        break
    position += move
    if position == 100:
        print("You are now on square 100")
        print("You Win!")
        break

    if position == 54:
        position = 19
    elif position == 90:
        position = 48
    elif position == 99:
        position = 77
    elif position == 9:
        position = 34
    elif position == 40:
        position = 64
    elif position == 67:
        position = 86
    elif position > 100:
        position -= move

    print("You are now on square " + str(position))

