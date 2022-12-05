'''

@author: BShefter25

Created on Oct 13, 2022
Updated on Oct 14, 2022
Updated on Oct 15, 2022
Updated on Oct 16, 2022

Bugs: There are no bugs

Description: Tic-Tac-Toe, where the user inputs a number 1 through nine
             and then the program will take their input, put it into the board,
             which will prompt the computer to return a number not including
             the one that the user picked, and the game will continue until all 
             nine spaces are filled or their is three straight, across, or 
             diagonally.

'''

def win(gameboard):
    if gameboard[0][0] == "X" and gameboard[0][1] == "X"  and gameboard[0][2] == "X": #checking rows
        print("\nX Wins!") #print X wins
        return True
    if gameboard[1][0] == "X" and gameboard[1][1] == "X" and gameboard[1][2] == "X": #checking rows
        print("\nX Wins!") #print X wins
        return True
    if gameboard[2][0] == "X" and gameboard[2][1] == "X" and gameboard[2][2] == "X": #checking rows
        print("\nX Wins!") #print X wins
        return True  
    if gameboard[0][0] == "X" and gameboard[1][1] == "X" and gameboard[2][2] == "X": #checking diagonals
        print("\nX Wins!") #print X wins
        return True
    if gameboard[0][2] == "X" and gameboard[1][1] == "X" and gameboard[2][0] == "X": #checking diagonals
        print("\nX Wins!") #print X wins
        return True
    if gameboard[0][0] == "X" and gameboard[1][0] == "X" and gameboard[2][0] == "X": #checking columns
        print("\nX Wins!") #print X wins
        return True
    if gameboard[0][1] == "X" and gameboard[1][1] == "X" and gameboard[2][1] == "X": #checking columns
        print("\nX Wins!") #print X wins
        return True
    if gameboard[0][2] == "X" and gameboard[1][2] == "X" and gameboard[2][2] == "X": #checking columns
        print("\nX Wins!") #print X wins
        return True
    
    if gameboard[0][0] == "O" and gameboard[0][1] == "O"  and gameboard[0][2] == "O": #checking rows
        print("\nO Wins!") #print O wins
        return True
    if gameboard[1][0] == "O" and gameboard[1][1] == "O" and gameboard[1][2] == "O": #checking rows
        print("\nO Wins!") #print O wins
        return True
    if gameboard[2][0] == "O" and gameboard[2][1] == "O" and gameboard[2][2] == "O": #checking rows
        print("\nO Wins!") #print O wins
        return True
    
    if gameboard[0][0] == "O" and gameboard[1][1] == "O" and gameboard[2][2] == "O": #checking diagonals
        print("\nO Wins!") #print O wins
        return True
    if gameboard[0][2] == "O" and gameboard[1][1] == "O" and gameboard[2][0] == "O": #checking diagonals
        print("\nO Wins!") #print O wins
        return True
    
    if gameboard[0][0] == "O" and gameboard[1][0] == "O" and gameboard[2][0] == "O": #checking columns
        print("\nO Wins!") #print O wins
        return True
    if gameboard[0][1] == "O" and gameboard[1][1] == "O" and gameboard[2][1] == "O": #checking columns
        print("\nO Wins!") #print O wins
        return True
    if gameboard[0][2] == "O" and gameboard[1][2] == "O" and gameboard[2][2] == "O": #checking columns
        print("\nO Wins!") #print O wins
        return True
    
    else:
        return False #else, keep going with program

def board(gameboard):
    for i in gameboard:
        print(i) #printing the board

def play_again(gameboard):
    try_again = input("Want To Play Again? ") #asking user if they want to play again
    while try_again not in "Yes" or "No":
        try_again = input("\nAre You Serious Right Now? Want To Play Again? <Y>es or <N>o? >: ") #re-ask the question
    if try_again == "Yes": #if they say yes
        start(gameboard) #restarts program
    elif try_again == "No": #if they say no
        print("Goodbye!") #end the code

def start(gameboard):                              
    print("\nPlayer 1, It Is Your Turn") #determines turn
    player1 = int(input("Pick A Number 1 Through 9: ")) #setting player1 equal to input
    space_checker(gameboard, player1) #checking to see space is open or taken
    while player1 not in range(1, 10): #if not through 1-10 then...
        player1 = int(input("\nAre You Serious Right Now? Pick A Number 1 Through 9: ")) #re-ask the question 
        
    if player1 == 1: #if they choose that spot
        gameboard[0][0] = "X" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player1 == 2: #if they choose that spot
        gameboard[0][1] = "X" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player1 == 3: #if they choose that spot
        gameboard[0][2] = "X"  #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player1 == 4: #if they choose that spot
        gameboard[1][0] = "X"  #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player1 == 5: #if they choose that spot
        gameboard[1][1] = "X" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player1 == 6: #if they choose that spot
        gameboard[1][2] = "X" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player1 == 7: #if they choose that spot
        gameboard[2][0] = "X" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player1 == 8: #if they choose that spot
        gameboard[2][1] = "X" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player1 == 9: #if they choose that spot
        gameboard[2][2] = "X" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    if win(gameboard) == True: #if the x has three in a row, then the game ends
        print("The Game Is Over")
        play_again()
    
    print("\nPlayer 2, It Is Your Turn") #determines turn
    player2 = int(input("Pick A Number 1 Through 9: ")) #setting player1 equal to input
    space_checker(gameboard, player2) #checking to see space is open or taken
    while player1 not in range(1, 10): #if not through 1-10 then...
        player2 = int(input("\nAre You Serious Right Now? Pick A Number 1 Through 9: ")) #re-ask the question 
        player2 = int(input("\nAre You Serious Right Now? Pick A Number 1 Through 9: ")) #re-ask the question
    
    if player2 == 1: #if they choose that spot
        gameboard[0][0] = "O" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player2 == 2: #if they choose that spot
        gameboard[0][1] = "O" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player2 == 3: #if they choose that spot
        gameboard[0][2] = "O" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player2 == 4: #if they choose that spot
        gameboard[1][0] = "O" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player2 == 5: #if they choose that spot
        gameboard[1][1] = "O" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player2 == 6: #if they choose that spot
        gameboard[1][2] = "O" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player2 == 7: #if they choose that spot
        gameboard[2][0] = "O" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player2 == 8: #if they choose that spot
        gameboard[2][1] = "O" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    elif player2 == 9: #if they choose that spot
        gameboard[2][2] = "O" #if player 1 chooses that spot, then fill it with an X
        board(gameboard) #print the gameboard replacing that spot
    
    if win(gameboard) == True: #if there is a win
        print("") #print a space
        play_again() #run the play again function
    elif win(gameboard) == False: #if no win
        start(gameboard) #continue
    
def space_checker(gameboard, player1):
    if player1 == 1:
        return gameboard[0][0]
    elif player1 == 2:
        return gameboard[0][1]
    elif player1 == 3:
        return gameboard[0][2]
    elif player1 == 4:
        return gameboard[1][0]
    elif player1 == 5:
        return gameboard[1][1]
    elif player1 == 6:
        return gameboard[1][2]
    elif player1 == 7:
        return gameboard[2][0]
    elif player1 == 8:
        return gameboard[2][1]
    elif player1 == 9:
        return gameboard[2][2]

def space_checker2(gameboard, player2):
    if player2 == 1:
        return gameboard[0][0]
    elif player2 == 2:
        return gameboard[0][1]
    elif player2 == 3:
        return gameboard[0][2]
    elif player2 == 4:
        return gameboard[1][0]
    elif player2 == 5:
        return gameboard[1][1]
    elif player2 == 6:
        return gameboard[1][2]
    elif player2 == 7:
        return gameboard[2][0]
    elif player2 == 8:
        return gameboard[2][1]
    elif player2 == 9:
        return gameboard[2][2]


def main():
    
    if space_checker(gameboard, player1) == "X" or space_checker(gameboard, player2) == "O":
        
    
    print("\n                                                         Welcome To TicTacToe\n")
    print("Player 1, You Are X & Will Go First")
    print("Player 2, you are O \n") #
        
    gameboard = [[ "1" , "2" , "3" ], [ "4" , "5" , "6" ], [ "7" , "8" , "9" ]] #creating the board
    board(gameboard) #print board(gameboard)
    
    start(gameboard) #run the start function

if __name__ == '__main__':
    main()