'''

@author: BShefter25

Created on Oct 10, 2022
Updated on Oct 11, 2022
Updated on Oct 18, 2022
Updated on Nov 14, 2022

Bugs: 

Description: Reverses the order of the characters starting at 
             position s with a length of l

'''

choice_input = 0
full_word = 0
character = 0


def reverse(running_str, first, final):
    
    full_word = running_str
    choice_input = running_str                                                    #setting choice = to full_words
    
    first = int(running_str)
    final = int(running_str)
    
    control = choice_input[first:final]                                         #setting bensvariable = choice_input
    output = ''                                                                 #output = space
    for i in range(len(control)-1,-1,-1):                                       #reversing the output
        output = output + control[i]                                            #output = variable + output
    
    character = len(full_word)                                                  #finding how many characters there are in the word
    slice_obj1 = slice(0, first)                                                #slicing the 0 letter to the starting user input
    slice_obj2 = slice(first, final)                                            #slicing the user input start and the user input end
    slice_obj3 = slice(final, character)                                        #slicing the final user input to the last character in the string
    
    beginning = full_word[slice_obj1]                                            #setting the beginning of the word equal to the first slice
    middle = full_word[slice_obj2]                                              #setting the middle of the word equal to the second slice
    ending = full_word[slice_obj3]                                              #setting the end of the word equal to the third slide
    
    for i in range(len(middle)-1,-1,-1):                                        #reversing the output
        output_1 = output + middle[i]                                           #setting output equal to the middle plus initial output
    output_1 = beginning + output + ending                                      #adding the revered output to the beginning and end output
    
    print("the new word is", output_1)