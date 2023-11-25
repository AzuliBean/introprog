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

"""
#övning 4  
# 
import random
     
def bingo_Card():
    def playfield():  
        grid_size = 45

        columns = 5
        rows = 7  # Adjust this based on the total number of elements (35) and the number of columns (5)
        my_list = []

        #where the start of the range is, if it's set to 1 it will start counting at 1
        counter = 11
        #creats rows for each playfield
        for i in range(rows):
            #creats a empty "row" list that will be put into the "my list" list
            row = []
            for j in range(columns):
                if counter <= 45:
                    #adds  what the current counter is into the row that then gets put into the list
                    row.append(counter)
                    #increases the counter by 1
                    counter += 1
            #adds the row to the playfield
            my_list.append(row)

        # Print the resulting list
        return my_list

    def bingo():
        #create variables that make up the row of playfields
        pf, pf1, pf2, pf3, pf4 = playfield(), playfield(), playfield(), playfield(), playfield()
        #lines up the rows next  to  eachother using zip and end = " "
        for row1, row2, row3, row4, row5 in zip(pf, pf1, pf2, pf3, pf4):
            print(row1, end=" ")
            print(row2, end=" ")
            print(row3, end=" ")
            print(row4, end=" ")
            print(row5)

    #creates a "GUI"  to make the bingo card look better
    print("- - - - - - - - - - - - - - - - - - - - - - - -BINGO CARD- - - - - - - - - - - - - - - - - - - - - - - -")
    bingo()
    print()
    bingo()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

#defines the range of random numbers that can be generated 
def generate_winning_numbers():
    return [random.randint(11, 45) for _ in range(7)]
#defines the how many winning rows and that they should be empty lists in the start
def generate_winning_row():
    winning_rows = 10
    row = []
    #generates the random numbers for the rows and then inserts them into the winning rows
    for _ in range(winning_rows):
        winning_row = generate_winning_numbers()
        row.append(winning_row)

    return row
#prints out all of the 10 rows that are the winning numbers 
def wins():
    row = generate_winning_row()

    for i, winning_row in enumerate(row, start=1):
        print(f"row {i}: {winning_row}")

bingo_Card()
print()
print("The winning numbers for each playfield are the following:")
wins()
"""


#övning 5
import random
#creates a empty list to store all the top scores
top_Scores = []

#creates a start variable so that the while case can start
answer = str.lower(input("Write start to start the game: "))
while answer != "stop":
    #asks if user wants to generate  a value or stop the porgram
    answer = str.lower(input("\nType Generate to get a score \nType Stop to end the game \nwhat do you want to do: "))
    #if answered generate this case will start
    if answer == "generate":
        #generates a random score from 0 - 1000
        score = random.randint(0, 1000)
        #checks the length of the list and if it's smaller than 10 then it will just automatically add the newly generated score to the list
        if len(top_Scores) < 10:
            top_Scores.append(score)
        #if the length of the list is bigger than 10 then start doing this
        else:
            #creates a variable that stores the smallest value from  the list
            min_Score = top_Scores.index(min(top_Scores))
            #checks if the newlygenerated score is bigger than the smallest score currently in the list
            if score > top_Scores[min_Score]:
                #replaces the smallest score with the newly generated score that was larger
                top_Scores[min_Score] = score
    #sorts the list with the largest score at the top
    top_Scores.sort(reverse=True)
    print(top_Scores)
            
print("\n The top scores are the following")
n = 1
for i in top_Scores:
    
   #printseevery score in the list individually to create a scoreboard
    print("\n", str(n), " - ", i, "points")
    n += 1
