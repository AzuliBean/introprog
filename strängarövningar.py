"""
#övning 1 
#variable med string 
lite_text = "Hejsan hoppsan i lingonskogen"

#skapar en variable som använder split för att skapa en lista av alla ord i stringen
ord_lista = str.split(lite_text)

#printar variablen
print(ord_lista)
"""

"""
#övning 2
#defines a function that counts the different things 
def character_counts(input_string):
    space_Count = 0
    tab_Count = 0
    other_Count = 0

    #checks everything within the () when the function is called
    for characters in input_string:
        #if there is a space it adds to the space counter 
        if characters == " ":
            space_Count += 1
        #if there is tab in the string the it adds to the tab counter
        elif characters == "\t":
            tab_Count += 1 
        #if there is anything else then it adds to the other counter
        else:
            other_Count += 1 
    #give all the answers that are stored 
    return space_Count, tab_Count, other_Count
#asks user for a input
user_Input = input("Input a sentance: ")
#creates variables that inherit their calue from the function character counter
spaces, tabs, others = character_counts(user_Input)
#prints out the sentance and all the stats on the sentance
print("You wrote the following sentance:\n", str(user_Input),"\n\nYour sentance contains\n", str(spaces), " amount of spaces\n", str(tabs), " amount of tabs\n", str(others), " amount of other characters" )
"""

"""
#övning 3
#defines a function that counts the capitlized and lower case letters
def letter_Check(input_String):
    #creates variables that store the data 
    cap_Letters = 0
    letters =  0
    #creates a for loop that goes through all of the letters in the sting that gets input 
    for characters in input_String:
        #if the character is lower then it adds to the counter
        if characters.islower():
            letters += 1 
        #if the character is upper then it adds to the counter
        elif characters.isupper():
            cap_Letters += 1 

    return letters, cap_Letters
#asks user for a input 
user_Input = input("Please input a sentance: ")
#creates variables that get their data from the function
cap, small = letter_Check(user_Input)
#prints the string along with the stats
print("\nYou wrote the following sentance:\n", str(user_Input),"\n\nYour sentance contains:\n", str(cap), " amount of capitalized letters\n", str(small), " amount of lower case letters\n")
"""


#övning 4
#uses list comprehension
def find_Startindex(string, substring):
    return [start for start in range(len(string)) if string.startswith(substring,start)]
#accepts user inputs
user_Input = input("please input your string: ")
user_Subinput = input("please input your sub string: ")
#find start indices
result = find_Startindex(user_Input, user_Subinput)
print(f"Start indices of occurrences of '{user_Subinput}': {result}")