'''

@author: BShefter25

Created on Sep 8, 2022
Updated on Sep 13, 2022
Updated on Sep 15, 2022
Updated on Sep 27, 2022
Updated on Sep 28, 2022
Updated on Sep 29, 2022
Updated on Oct 1, 2022
Updated on Oct 6, 2022
Finished on Feb 21, 2022

Bugs: There are no bugs

Description: My program uses if statements, inputs, variables, and equations 
             to determine how much it will cost to ship their package through 
             however many zones.

'''

def get_type(length_input, height_input, width_input):
   
    type_1 = 0
    
    if 3.5 <= length_input <= 4.25 and 3.5 <= height_input <= 6 and .007 <= width_input <= .016:                               #user_input >= 3.5 and user_input <= 4.25
        type_1 = 1
        
    elif 4.25 <= length_input <= 6 and 6 <= height_input <= 11.5 and .007 <= width_input <= .015:                              #making an inequality to find the data between two numbers
        type_1 = 2 
        
    elif 3.5 <= length_input <= 6.125 and 5 <= height_input <= 11.5 and .016 <= width_input <= .25:                            #making an inequality to find the data between two numbers
        type_1 = 3
        
    elif 6.125 <= length_input <= 24 and 11 <= height_input <= 18 and .25 <= width_input <= .5:                                #making an inequality to find the data between two numbers
        type_1 = 4
        
    elif length_input > 24 and height_input > 18 and width_input > .5 and length_input + 2*(length_input + width_input) <= 84: #making an inequality to find the data between two numbers
        type_1 = 5
        
    elif 84 <= (length_input + 2*(length_input + width_input)) and (length_input + 2*(length_input + width_input)) <= 130:     #making an inequality to find the data between two numbers
        type_1 = 6
    
    else:                                                                                                                      #if none of the statements above work, then it will print out un-mailable
        print("Your Package Is Unmailable... We Cannot Do Anything Else")                                                      #printing output for the user
    
    return type_1
        
    
    
def get_zip(zip_code):
    
    if zip_code >= 1 and zip_code <= 6999:                                                          #if the zip-code is between 00001 and 06999...
        start_zone = 1                                                                              #then the starting zone is 1
    
    elif zip_code >= 7000 and zip_code <= 19999:                                                    #if the zip-code is between 07000 and 19999...
        start_zone = 2                                                                              #then the starting zone is 2  
    
    elif zip_code >= 20000 and zip_code <= 35999:                                                   #if the zip-code is between 20000 and 35999...
        start_zone = 3                                                                              #then the starting zone is 3
        
    elif zip_code >= 36000 and zip_code <= 62999:                                                   #if the zip-code is between 36000 and 62999...
        start_zone = 4                                                                              #then the starting zone is 4
        
    elif zip_code >= 63000 and zip_code <= 84999:                                                   #if the zip-code is between 63000 and 84999...
        start_zone = 5                                                                              #then the starting zone is 5
    
    elif zip_code >= 85000 and zip_code <= 99999:                                                   #if the zip-code is between 85000 and 99999...
        start_zone = 6                                                                              #then the starting zone is 6 


    return start_zone                                                                               #returning the output to the user


def get_price(type_1, total_zone):    

    if type_1 == 1:                                                                                 #if the type is 1 (regular postcard) then it will cost...
        cost = 0.2 + (total_zone * 0.03)                                                            #0.20 plus the total amount of zones passed times 0.03
        
    elif type_1 == 2:                                                                               #if the type is 2 (large postcard) then it will cost...
        cost = 0.37 + (total_zone * 0.03)                                                           #0.37 plus the total amount of zones passed times 0.03
    
    elif type_1 == 3:                                                                               #if the type is 3 (envelope) then it will cost...
        cost = 0.37 + (total_zone * 0.04)                                                           #0.37 plus the total amount of zones passed times 0.04
    
    elif type_1 == 4:                                                                               #if the type is 4 (large envelope) then it will cost...
        cost = 0.60 + (total_zone * 0.05)                                                           #0.60 plus the total amount of zones passed times 0.05
    
    elif type_1 == 5:                                                                               #if the type is 5 (package) then it will cost...
        cost = 2.95 + (total_zone * 0.25)                                                           #2.95 plus the total amount of zones passed times 0.25
    
    elif type_1 == 6:                                                                               #if the type is 6 (large package) then it will cost...
        cost = 3.95 + (total_zone * 0.35)                                                           #3.95 plus the total amount of zones passed times 0.35
    
    return cost
    


def main(): 
   
    cost = 0                                                                                        #Setting the variable equal to 0 because it is a number
    type_1 = 0                                                                                      #Setting the variable equal to 0 because it is a number
    total_zone = 0                                                                                  #Setting the variable equal to 0 because it is a number
    start_zone = 0                                                                                  #Setting the variable equal to 0 because it is a number
    end_zone = 0                                                                                    #Setting the variable equal to 0 because it is a number
    zip_code = 0                                                                                    #Setting the variable equal to 0 because it is a number
    end_zip = 0                                                                                     #Setting the variable equal to 0 because it is a number
    
    print("                                                Let's Find The Size of Your Mail \n")    
    length_input = float(input("What Is The Length of Your Package? "))
    height_input = float(input("What Is The Height of Your Package? "))
    width_input = float(input("What Is The Width of Your Package? "))
    
    type_1 = get_type(length_input, height_input, width_input)                                          #getting the type of the users package
    
    from_zip_code = int(input("\nWhere Is Your Package Coming From? "))                                 #setting the user input equal to zip_code
    start_zone = get_zip(from_zip_code)                                                                 #calling the get_zip function
    
    to_zip_code = int(input("Where Is Your Package Going To? "))                                        #setting the user input equal to zip_code
    end_zone = get_zip(to_zip_code)                                                                     #calling the get_end_zip function
    
    total_zone = abs(start_zone-end_zone)                                                               #creating an absolute value equation in order to find how many zones it is going through, the absolute value equation makes this number always positive

    total_cost = get_price(type_1, total_zone)                                                          #setting the total cost equal to type_1 and total_zone

    print("\nYour Package Is Going Through", total_zone, "Zones")                                       #printing out the total zones in a clean format

    print("The Final Cost of Your Package Is", total_cost)                                              #printing out the end cost in a clean format


if __name__ == '__main__':
    main()