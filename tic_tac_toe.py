
import random

print("Welcome to Tic Tac Toe")
player1 = input("Enter your name: ")
player2 = input("Enter your name: ")

def show(matrix):
    print("Here's the grid")
    for row in matrix:
        for element in row:
            print(element, end = ' ')
        print()

print("Welcome " + player1 + " and " + player2)
order = int(input("Let's play! \nwho wants to go first? type 1 for {a}, 2 for {b}: ".format(a=player1,b=player2)))
print(order)

if order == 1:
    first = player1
    second = player2
    print("yay")
else:
    first = player2
    second = player1

grid = [["","",""],["","",""],["","",""]]
show(grid)
i = 0
play = True

def check_row(matrix):
    won = False
    for row in matrix:
        sum= 0
        for element in row:
            if element == "":
                break
            sum = sum+element
        if sum == 3 or sum == 24:
            won = True
    return won

def check_col(matrix):
    won = False
    for i in range(0,3):
        sum = 0
        for row in matrix:
            if row[i] == "":
                break
            sum = sum + row[i]
            if sum == 3 or sum == 24:
                won = True
    return won

def check_diag(matrix):
    won = False
    diag1 = 0
    for row in range(0,3):
        for element in range(0,3):
            if row == element:
                if matrix[row][element] == "":
                    break
                diag1 = diag1 + matrix[row][element]

    diag2 = 0
    if matrix[0][2] == "" or matrix[1][1] == "" or matrix[2][0] == "":
        won = False   
    else:
        diag2 = matrix[0][2] + matrix[1][1] + matrix[2][0]
    
    if diag1 == 3 or diag1 == 24 or diag2 == 3 or diag2 == 24:
        won = True
    return won 
print("{} you are 1, {} you are 8".format(first, second))
while play == True:
    f = True
    while f == True:
        frow = int(input("{} enter row of your move: ".format(first)))
        fcol = int(input("{} enter column of your move: ".format(first)))
        if grid[frow][fcol] == "":
            grid[frow][fcol] = 1
            f = False 
        else:
            print("There's already an element there, try again")
    c1 = check_row(grid)
    c2 = check_col(grid)
    c3 = check_diag(grid)
    show(grid)
    if c1 == True or c2 == True or c3 == True:
        print("{} won".format(first))
        play = False
        break
    i=i+1
    if i==9:
        print("It's a Draw")
        play = False
        break
    s = True
    while s == True:
        srow = int(input("{} enter row of your move: ".format(second)))
        scol = int(input("{} enter column of your move: ".format(second)))
        if grid[srow][scol] == "":
            grid[srow][scol] = 8
            s = False 
        else:
            print("There's already an element there, try again")
    c1 = check_row(grid)
    c2 = check_col(grid)
    c3 = check_diag(grid)
    show(grid)
    if c1 == True or c2 == True or c3 == True:
        print("{} won".format(second))
        play = False
        break
    i=i+1


