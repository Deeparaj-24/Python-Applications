import json as js
import difflib
 # json is a way of representing data, like a format
#step 1 We created a function to open a dict and we defined a function to retun our search
#Step 2 To make it user friendly add display a message in case the user gets it wrong
#Step 3 To make the pgm work irrespective of the case add lower method
#Step 4 Spelling error should be handled .ie we are going to do some function for smililar word using diff difflib
from difflib import get_close_matches
data = js.load(open('data.json'))# Loading data.json into a var
def dt(w):# need not use a specific var name as it is only local
    w = w.lower()
    if w in data :
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len (get_close_matches(w,data.keys()) )>0  :
        yn = input( "Did you mean %s? \n If yes enter Y,if no enter N: " %get_close_matches(w,data.keys())[0])#Displays similar word
        if yn == 'Y' :
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N' :
            return "The word that you entered does not exist."
        else :
            return "We did not understand your entry."
    else :
        return "The word does not exist,please double check."
word = input("Please enter the word: ")
output = (dt(word))
if type(output) == list :
    for items in output :
        print(items)
else :
    print(output)
