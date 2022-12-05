'''

@author: BShefter25

Created on Oct 1, 2022

Bugs: There are no bugs

Description: Program that simulates the game of battleship

'''

from random import randint

def randomplace():
    return randint(1, 5), randint(1, 5) #creating a random place for each of the ships
   
def gameover():
    print("You Have 0 Shots Left! Game Over!")
    playagain()

def play_game():
    print("                                                      WELCOME TO BATTLESHIP\n")
    board = [['  1 2 3 4 5' , ] , [1, "O", "O", "O", "O", "O"],
                  [2, "O", "O", "O", "O", "O"],
                  [3, "O", "O", "O", "O", "O"],
                  [4, "O", "O", "O", "O", "O"],
                  [5, "O", "O", "O", "O", "O"]]
    for i in board:
        print(*i)               #i'm making the grid

    battleship1 = randomplace() #creating random ship point for ship 1
    battleship2 = randomplace() #creating random ship point for ship 2
    battleship3 = randomplace() #creating random ship point for ship 3
    shipcounter = 3             #shows how many ships are left
    shots = 25                  #shows how many shots or tries are left

    while shots:                #while they have shots left
        try:
            row = int(input("\nEnter A Row Number Between 1 & 5: "))        #asking for a row
            column = int(input("Enter A Column Number Between 1 & 5: "))    #asking for a column
        except row not in range (1, 6) or column not in range (1, 6):       #while the input is not between those numbers...
            print("\nThe Numbers Must Be Between 1 & 5!")                   #print the statement                                                                 #since i have an extra column I have to subtract 1 from the players input
        column = column                                                     #setting column equal to column
        
        if board[row][column] == "?" or board[row][column] == "X":                #if the spot is filled with a ? or X...
            print("\nYou Serious Right Now? You Have Already Chosen That Spot!")  #print the statement
            continue                                                              #once it is correct, move on
        
        elif (row, column) == battleship1 or (row, column) == battleship2 or (row, column) == battleship3:   #if the player hits the ship and therefore sinks it... 
            print("\nYou Hit A Ship! A Ship Has Been Destroyed! You Have Been Given A New Shot!\n")                                         #print the statement
            board[row][column] = "X"            #when they hit the ship, place an X in that spot
            shipcounter -= 1                     #minus 1 from the total number of ships
            if shipcounter == 0:                 #if there are 0 ships left...
                print("Congrats, You Won!")     #print that they win
                play_again()
    
        else:
            print("You Missed!\n")              #if they miss...
            board[row][column] = "?"            #place a ? at the missed spot
            shots -= 1                          #minus 1 from the total ships left
            
        for i in board:
            print(*i)                           #i'm making the grid
           
        print("You Have " + str(shots) + " Shots Left & There Are " + str(shipcounter) + " Ships Left") #printing output in a neat way
        
def play_again():
    try_again = input("Want To Play Again? ").lower()   #asking the user if they want to play again
    if try_again == "Yes":                              #if they say yes...
        play_game()                                     #run the play again function
    else:
        print("Ok, See Ya!")                            #otherwise, end the program
        return

def main():
    
    playagain()

if __name__ == "__main__":
    play_game()