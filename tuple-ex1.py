'''

@author: BShefter25

'''

emailfolder = open('mbox-short.txt', 'r')                  #OPENING THE FILE

emailing = {}

for line in emailfolder:                                   #CREATING A LOOP
    
    if line.startswith("From "):                           #IF THE LINE STARTS WITH FROM
    
        email = line.split()[1]                            #THEN EMAIL 
    
        emailing[email] = emailing.get(email, 0) + 1       #ADD ONE TO THE EMAIL FREQUENCY

lst = []                                                   #CREATING DICTIONARY

for key, value in emailing():                              #CREATING A LOOP BY RETURNING A LIST

    lst.append((value, key))                               #APPENDING THE VALUE AND KEY

lst.sort(reverse = True)                                   #MAKING IT PRINT OUT THE MOST RATHER THAN THE LEAST AMOUNT OF EMAILS

ptuple = lst[0]                                            #STARTS THE LST AT 0

print(ptuple[1], ptuple[0])                                #PRINTING OUT THE PERSON WHO HAS THE MOST EMAILS