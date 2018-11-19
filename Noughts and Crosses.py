import random

def menu():
    print("Noughts and Crosses\n1.Player Vs Player\n2.Player Vs Computer\n3.Quit")
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

def pvp():
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
            user(player_2_symbol,grid,player_number)
        win = win_con(grid)
        if win == "win":
            grid_printer(grid)
            print("Player " + str(player(player_number)) + " is the Winner!")
            break
        if turn == 9:
            grid_printer(grid)
            print("Tie")
            break
        player_number += 1

def cpu(symbol,grid):
    i = random.randint(1,10)
    while True:
        if grid[i] == " ":
            grid[i] = symbol
            return grid

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
        pvp()
    if user == 2:
        pve()
    if user == 3:
        print("Bye Bye!")
main()