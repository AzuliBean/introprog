"""
#övning 1
#take the first value
value_one = int(input("first number"))

#take the second value

value_two = int(input("second number"))

result = value_one * value_two

print(result)
"""

"""
#övning 2
#ask user for a number
number = int(input("hand over a number: "))

#set parameters for if a number is a 5:a or a 6:a
#checks if number is equal to 5 then:
if number == 5:
    print ("you wrote a 5")
#checks if number is equal to 6 then:
elif number == 6:
    print ("you wrote a 6")
"""

"""
#övning 3

#lists containng the values that make up the conditions
set1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
set2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
set3 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

#ask user for a value
number = int(input("hand over a value: "))

#check if the given value is in the first list
if number in set1:
    print ("blue")
#check if the given value is in the second list
elif number in set2:
    print ("red")
#check if the given value is in the third list
elif number in set3:
    print ("green")
#if the given value is outside of the 3 sets of conditions
else:
    print("no correct color values")
"""


"""
#övning 4
#variable that starts the count
num = 1

#while loop that runs while the number is inbetween 1 and 101
while num in range(1, 101):
    #checks if there is anything left when it's devided by 5
    if num % 5 == 0:
        print(num)  #print must be inside the condition
    num += 1  #the increase must be done on every iteration
"""


#övning 5
#variable that is the start number
num = 1
#ask user for what the end number should be for the range
user_Num = int(input("what should be the end of the number range: "))
#while loop that runs while the number is inbetween 1 and the user input
while num in range(1, user_Num):
    #checks if there is anything left when it's devided by 2
    if num % 2 == 0:
        #print must be inside the condition
        print(num) 
    #the increase must be done on every iteration
    num += 1 
