"""
#övning 1 & 2

#variable that is the start number
num = 1
counter = 1
#ask user for how many odd numbers they
user_Num = int(input("How many odd numbers do you want: "))
#while loop that runs as long as the count isn't equal to the given amount
if user_Num % 2 == 0:
    while counter <= user_Num:
        #checks if there is anything left when it's devided by 2 
        if num % 2 == 1:
            #print must be inside the condition
            #the increase is only added to the count when a number is printed
            print(num)
            counter += 1
        #the increase must be done on every iteration
        num += 1 
else:
    print("You have to input a even amount of odd number that you want")  
"""

"""
#övning 3 & 4 & 7

x = int(input("input the start of the number range: "))
y = int(input("input the end of the number range: "))
if y > x:
    for x in range (x, y):
        print(x, end = " ")
else:
    print("The end of the number range has to be larger than the start")
"""

"""
#övning 5
x = int(input("input the start of the number range: "))
y = int(input("input the end of the number range: "))
for x in range (y - 1, x - 1, -1):
    print(x, end = " ")
"""

"""
#övning 6
x = int(input("input the start of the number range: "))
y = int(input("input the end of the number range: "))
for x in range (x, y, 2):
    print(x, end = " ")
"""

"""
#övning 8 
x = int(input("input the start of the number range: "))
y = int(input("input the end of the number range: "))
counter = 0

for x in range (x, y):
    print(x, end = " ")
    counter += 1

    if counter == 10:
        print()
        counter = 0
"""

"""
#övning 9.4 9.5 9.7 

user_Start = int(input("what should be the start of the number range: "))
user_End = int(input("what should be the end of the number range: "))

if user_End >= user_Start:
    current_Spot = user_End - 1

    while current_Spot >= user_Start:
        print(current_Spot, end= " ")
        current_Spot -= 1
else:
    print("your end point has to be larger than the start!")
"""

"""
#övning 9.6
user_Start = int(input("what should be the start of the number range: "))
user_End = int(input("what should be the end of the number range: "))

current_Spot = user_Start
while current_Spot <= user_End:
    print(current_Spot, end = " ")
    current_Spot += 2
"""


#övning 9.8

counter = 0
user_Start = int(input("what should be the start of the number range: "))
user_End = int(input("what should be the end of the number range: "))

current_Spot = user_Start
while current_Spot <= user_End:
    print(current_Spot, end = " ")
    current_Spot += 1
    counter += 1 

    if counter == 10:
        print()
        counter = 0
