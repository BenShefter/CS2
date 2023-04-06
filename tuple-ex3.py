'''

@author: BShefter25

'''

alphabet = 'abcdefghijklmnopqrstuvxwyz'                 #CREATING THE ALPHABET
             
fhand = open('mbox-short.txt', 'r')                     #OPENING UP THE FILE

text = fhand.read()                                     #READING THE FILE  

freq_dict = {}                                          #FINDING THE FREQUENCY

for chapt in text.lower():                              #CREATING A FOR LOOP

    if chapt in alphabet:                               #IF THERE IS CHAPT IN THE ALPHABET

        freq_dict[chapt] = freq_dict.get(chapt, 0) + 1  #ADD 1 TO THE FREQUENCY TO THE RIGHT LETTER

list = []                                               #CREATIJNGN DICTIONARY

for key, value in freq_dict.items():                    #CREATING A LOOP

    list.append((value,key))                            #APPENDING THE FILE

list.sort(reverse = True)                               #SORTING THE LIST

for freq, letter in list:                               #CREATING A LOOP

    print(letter, freq)                                 #PRINTING OUT THE LETTER AND FREQUENCY