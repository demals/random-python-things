import random

def menu():
    print("Noughts and Crosses\n1.Player Vs Computer\n2.Quit")
    user = int(input())
    return user

def grid_help():
    print("how to pick grid space")
    print("1|2|3\n4|5|6\n7|8|9")
    return None

def grid(n,x_or_o,grid):
    grid[n] = x_or_o
    return grid

def grid_printer(grid):
    for i in range(1,10):
        if i % 3 == 0:
            print(grid[i])
        else:
            print(grid[i] + "|",end="")
    print()

def picker_1():
    symbols = ["X","O"]
    user_symbol = random.choice(symbols)
    return user_symbol

def picker_2(symbol):
    if symbol == "X":
        return "O"
    else:
        return "X"

def user(symbol,grid,p_number):
    user  = int(input("Player " + str(p_number) + " what space do you want? "))
    while True:
        if grid[user] == " ":
            grid[user] = symbol
            return grid
        else:
            user = int(input("you can't have that dude, pick another space: "))

def player(player_number):
    if player_number % 2 == 1:
        return 1
    else:
        return 2

def cpu(symbol,grid):
    return ai(symbol,grid)

def random_block(symbol,grid):
    while True:
        i = random.randint(1, 10)
        if grid[i] == " ":
            grid[i] = symbol
            return "ok"

def attack(symbol,grid):
    if (((grid[1] == grid[4]) and grid[1] == symbol) or ((grid[3] == grid[5]) and grid[3] == symbol) or ((grid[8] == grid[9]) and grid[8] == symbol)) and grid[7] == " ":
        grid[7] = symbol
        return "ok"
    elif (((grid[2] == grid[3]) and grid[2] == symbol) or ((grid[8] == grid[9]) and grid[8] == symbol) or ((grid[4] == grid[7]) and grid[4] == symbol)) and grid[1] == " ":
        grid[1] = symbol
        return "ok"
    elif (((grid[1] == grid[5]) and grid[1] == symbol) or ((grid[3] == grid[6]) and grid[3] == symbol) or ((grid[8] == grid[7]) and grid[8] == symbol)) and grid[9] == " ":
        grid[9] = symbol
        return "ok"
    elif (((grid[1] == grid[2]) and grid[1] == symbol) or ((grid[7] == grid[5]) and grid[7] == symbol) or ((grid[6] == grid[9]) and grid[6] == symbol)) and grid[3] == " ":
        grid[3] = symbol
        return "ok"
    elif (((grid[1] == grid[3]) and grid[1] == symbol) or ((grid[8] == grid[5]) and grid[5] == symbol)) and grid[2] == " ":
        grid[2] = symbol
        return "ok"
    elif (((grid[1] == grid[7]) and grid[1] == symbol) or ((grid[6] == grid[5]) and grid[5] == symbol)) and grid[4] == " ":
        grid[4] = symbol
        return "ok"
    elif (((grid[1] == grid[7]) and grid[1] == symbol) or ((grid[6] == grid[5]) and grid[5] == symbol)) and grid[4] == " ":
        grid[4] = symbol
        return "ok"
    elif (((grid[4] == grid[5]) and grid[4] == symbol) or ((grid[3] == grid[9]) and grid[3] == symbol)) and grid[6] == " ":
        grid[6] = symbol
        return "ok"
    elif (((grid[2] == grid[4]) and grid[2] == symbol) or ((grid[7] == grid[9]) and grid[9] == symbol)) and grid[8] == " ":
        grid[8] = symbol
        return "ok"
    elif (((grid[1] == grid[9]) and grid[1] == symbol) or ((grid[2] == grid[8]) and grid[2] == symbol) or ((grid[7] == grid[3]) and grid[7] == symbol) or ((grid[6] == grid[4]) and grid[6] == symbol)) and grid[5] == " ":
        grid[5] = symbol
        return "ok"
    else:
        return None
def block(symbol,grid):
    if (((grid[1] == grid[4]) and grid[1] != symbol) or ((grid[3] == grid[5]) and grid[3] != symbol) or ((grid[8] == grid[9]) and grid[8] != symbol)) and grid[7] == " ":
        grid[7] = symbol
        return "ok"
    elif (((grid[2] == grid[3]) and grid[2] != symbol) or ((grid[8] == grid[9]) and grid[8] != symbol) or ((grid[4] == grid[7]) and grid[4] != symbol)) and grid[1] == " ":
        grid[1] = symbol
        return "ok"
    elif (((grid[1] == grid[5]) and grid[1] != symbol) or ((grid[3] == grid[6]) and grid[3] != symbol) or ((grid[8] == grid[7]) and grid[8] != symbol)) and grid[9] == " ":
        grid[9] = symbol
        return "ok"
    elif (((grid[1] == grid[2]) and grid[1] != symbol) or ((grid[7] == grid[5]) and grid[7] != symbol) or ((grid[6] == grid[9]) and grid[6] != symbol)) and grid[3] == " ":
        grid[3] = symbol
        return "ok"
    elif (((grid[1] == grid[3]) and grid[1] != symbol) or ((grid[8] == grid[5]) and grid[5] != symbol)) and grid[2] == " ":
        grid[2] = symbol
        return "ok"
    elif (((grid[1] == grid[7]) and grid[1] != symbol) or ((grid[6] == grid[5]) and grid[5] != symbol)) and grid[4] == " ":
        grid[4] = symbol
        return "ok"
    elif (((grid[1] == grid[7]) and grid[1] != symbol) or ((grid[6] == grid[5]) and grid[5] != symbol)) and grid[4] == " ":
        grid[4] = symbol
        return "ok"
    elif (((grid[4] == grid[5]) and grid[4] != symbol) or ((grid[3] == grid[9]) and grid[3] != symbol)) and grid[6] == " ":
        grid[6] = symbol
        return "ok"
    elif (((grid[2] == grid[4]) and grid[2] != symbol) or ((grid[7] == grid[9]) and grid[9] != symbol)) and grid[8] == " ":
        grid[8] = symbol
        return "ok"
    elif (((grid[1] == grid[9]) and grid[1] != symbol) or ((grid[2] == grid[8]) and grid[2] != symbol) or ((grid[7] == grid[3]) and grid[7] != symbol) or ((grid[6] == grid[4]) and grid[6] != symbol)) and grid[5] == " ":
        grid[5] = symbol
        return "ok"
    else:
        return None

def ai(symbol,grid):
    if attack(symbol,grid) != None:
        return "ok"
    elif block(symbol,grid) != None:
        return "ok"
    else:
        return random_block()
def pve():
    grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "," "]
    grid_help()
    player_1_symbol = picker_1()
    player_2_symbol = picker_2(player_1_symbol)
    player_number = random.randint(1,3)
    turn = 0
    while True:
        turn += 1
        grid_printer(grid)
        player_number = player(player_number)
        if player_number == 1:
            user(player_1_symbol,grid,player_number)
        else:
            cpu(player_2_symbol,grid)
        win = win_con(grid)
        if win == "win":
            grid_printer(grid)
            if player_number == 1:
                print("you won!")
                break
            else:
                print("you lost")
                break
        if turn == 9:
            grid_printer(grid)
            print("Tie")
            break
        player_number += 1

def win_con(grid):
    if grid[1] == grid[2] == grid[3] and grid[1] != " " and grid[2] != " " and grid[3] != " ":
        return "win"
    if grid[4] == grid[5] == grid[6] and grid[4] != " " and grid[5] != " " and grid[6] != " ":
        return "win"
    if grid[7] == grid[8] == grid[9] and grid[7] != " " and grid[8] != " " and grid[9] != " ":
        return "win"
    if grid[1] == grid[4] == grid[7] and grid[1] != " " and grid[4] != " " and grid[7] != " ":
        return "win"
    if grid[2] == grid[5] == grid[8] and grid[2] != " " and grid[5] != " " and grid[8] != " ":
        return "win"
    if grid[3] == grid[6] == grid[9] and grid[3] != " " and grid[6] != " " and grid[9] != " ":
        return "win"
    if grid[1] == grid[5] == grid[9] and grid[1] != " " and grid[5] != " " and grid[9] != " ":
        return "win"
    if grid[3] == grid[5] == grid[7] and grid[1] != " " and grid[5] != " " and grid[7] != " ":
        return "win"

def main():
    user = menu()
    if user == 1:
        pve()
    if user == 2:
        print("Bye Bye!")
main()
