#övning 1

#variable that is the start number
num = 1
counter = 1
#ask user for how many odd numbers they
user_Num = int(input("How many odd numbers do you want: "))
#while loop that runs as long as the count isn't equal to the given amount
while counter <= user_Num:
    #checks if there is anything left when it's devided by 2 
    if num % 2 == 1:
        #print must be inside the condition
        #the increase is only added to the count when a number is printed
        print(num)
        counter += 1
    #the increase must be done on every iteration
    num += 1 
    
