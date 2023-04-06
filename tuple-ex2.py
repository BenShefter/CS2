'''

@author: BShefter25

'''
import urllib.request  #the lib that handles the url stuff

with urllib.request.urlopen('http://www.py4inf.com/code/mbox.txt') as file:

    hourd = []
    
    for line in file: 
    
        line = str(line)                                             #CREATING A LOOP
    
        if line.startswith("From "):                                #FINDING THE TIME STAMPS
    
            time = line.split()[5]                                  #SPLITTING THE LINE FOR TIME
    
            hour = time.split(":")[0]                               #SPLITTING THE LINE FOR HOUSE
    
            hourd[hour] = hourd.get(hour, 0) + 1                #ADDING 1 TO THE COUNTER WHEN IT FINDS AN HOUR

list = list(hourd)                                              #SETTING A VARIABLE EQUAL TO THE ITEMS LIST

list.sort()                                                     #SORTING THE LIST

for tuple in list:                                              #CREATING A LOOP

    print(tuple[0], tuple[1])                                   #PRINTING OUT THE TIME AND THE FREQUENCY