"""
#övning 1

#creats a empty list and creats a start and end for the range
amount = 0
user_List = []
counter = int(input("how many numbers do you want in your list: "))

#creates a while loop that continues as long as the variable amount is smaller than the variable counter
while amount < counter:
    #asks user for a number that they want to input into the list
    entry = int(input("please input your value: "))
    #inputs the given answer into the list using append
    user_List.append(entry)
    #increases the current counter 
    amount += 1
#prints the now completed list.
print (user_List)
"""

"""
#övning 2

#creats a empty list and creats a start and end for the range
amount = 0
user_List = []
counter = int(input("how many numbers do you want in your list: "))

#creates a while loop that continues as long as the variable amount is smaller than the variable counter
while amount < counter:
    #asks user for a number that they want to input into the list
    entry = int(input("please input your value: "))
    #inputs the given answer into the list using append
    user_List.append(entry)
    #increases the current counter 
    amount += 1
#prints the now completed list.
print("this is the old unfiltered list " + str(user_List))

#creates a list that looks for the values in the old list(user_List) that are bigger than 451 using a if case that checks if "value" in user_list is bigger than 451 and if it is then adds it to the current list)
filtered_List = [value for value in user_List if value > 451]
print("here is the list of values you input that are greater than 451 " + str(filtered_List))
"""

"""
#övning 3 
#creates a empty list for all the names aswell as a counter for how many times the name kalle has been written down
names = []
kalle_Counter = 0

#asks the user to input a name and stores it in a variable
name_Input = str.lower(input("please write down a name that you want to enter the list: "))

#creates a loop that is active as long as the stored value inside the variable isn't "stop"
while name_Input != "stop":
    #creates a conditon that if the stored value inside the variable is "kalle"
    if name_Input == "kalle":
        #inserts the value to the list
        names.append(name_Input)
        #increases the counter keeping check of how many times kalle has been written
        kalle_Counter += 1
        #asks the user to input another name or if they want to stop the program
        name_Input = str.lower(input("please input another name you want to add to the list \nTo stop the program please write stop: "))
    else:
        #if the value in the vairable isn't kalle it will just input the value to the list without adding to the kalle counter as well as asking if the user wants to continue or not
        names.append(name_Input)
        name_Input = str.lower(input("please input another name you want to add to the list \nTo stop the program please write stop: "))

#sorts the names in alphabetical order and then prints out how many times the user has written the name kalle as well as showing all the names the user has written in a list
names.sort()      
print("You've ended the program here are some stats: \n\nYou've written the name Kalle " + str(kalle_Counter) + "times in total. \nHere is a list of all the names you have written down\n" + str(names) )
"""


#övning 4 

def playfield():  
    grid_size = 35

    columns = 5
    rows = 7  # Adjust this based on the total number of elements (35) and the number of columns (5)
    my_list = []

    counter = 1
    for i in range(rows):
        row = []
        for j in range(columns):
            if counter <= 35:
                row.append(counter)
                counter += 1
        my_list.append(row)

    # Print the resulting list
    for row in my_list:
        print(row)

def bingo_Card():
    counter = 0
    while counter != 10:
        playfield()
        counter += 1
        
        if counter == 5:
            print()
        
    
bingo_Card()

    
"""
import random

def generera_vinnande_rad():
    return [random.randint(1, 35) for _ in range(7)]

def generera_spelfalt():
    antal_spelfalt = 10
    spelfalt = []

    for _ in range(antal_spelfalt):
        vinnande_rad = generera_vinnande_rad()
        spelfalt.append(vinnande_rad)

    return spelfalt

def main():
    spelfalt = generera_spelfalt()

    for i, vinnande_rad in enumerate(spelfalt, start=1):
        print(f"Spelfält {i}: {vinnande_rad}")

if __name__ == "__main__":
    main()
"""