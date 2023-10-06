# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_table(inputs):
    for i in range(3):
        for j in range(3):
            print(inputs[i][j], "| ", end="")
        print("\n--+---+----")

def get_input(inputs, turn):
    print("Choose between 1 and 9 according to the available positions")
    print_table(inputs)
    x=int(input("Player" +  turn + ": "))
    for i in range(3):
        for j in range(3):
            #print(i)
            if inputs[i][j]==x:
                inputs[i][j]=turn
                break

def check_win(inputs):
    if inputs[0][0]==inputs[0][1]==inputs[0][2]:
        print("We have a winner")
        exit(0)
    elif inputs[1][0]==inputs[1][1]==inputs[1][2]:
        print("We have a winner")
        exit(0)
    elif inputs[2][0]==inputs[2][1]==inputs[2][2]:
        print("We have a winner")
        exit(0)
    elif inputs[0][0]==inputs[1][1]==inputs[2][2]:
        print("We have a winner")
        exit(0)
    elif inputs[0][2]==inputs[1][1]==inputs[2][0]:
        print("We have a winner")
        exit(0)
    elif inputs[0][0]==inputs[1][0]==inputs[2][0]:
        print("We have a winner")
        exit(0)
    elif inputs[0][1]==inputs[1][1]==inputs[2][1]:
        print("We have a winner")
        exit(0)
    elif inputs[0][2]==inputs[1][2]==inputs[2][2]:
        print("We have a winner")
        exit(0)
    return 0

def game():
    inputs=[[1,2,3],
            [4,5,6],
            [7,8,9],]
    turn = 'X'
    for i in range(9):
        get_input(inputs, turn)
        check_win(inputs)

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        if i == 8:
            print("No one won...")
            exit(0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
