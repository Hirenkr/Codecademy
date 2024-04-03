
import random

print("Welcome to Tic Tac Toe")
player1 = input("Enter your name: ")
player2 = input("Enter your name: ")

print("Welcome " + player1 + " and " + player2)
order = input("Let's play: \nwho wants to go first? type 1 for {a}, 2 for {b}".format(a=player1,b=player2))
