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
