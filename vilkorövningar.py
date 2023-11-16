from random import randint

"""
#övning 4
x = int(input("input a value: "))

#checks if the input can be divided with 2 without leaving behind decimals
if x % 2 == 0:
    print(str(x) + " är ett jämt tal")
else:
    print(str(x) + " är ett udda tal")
"""

"""
#övning 5
x = int(input("input a value: "))

#checks if the input can be divided whole with 9 without leaving behind decimals
if x % 9 == 0:
    print(str(x) + " kan delas helt med 9")
else:
    print(str(x) + " kan inte delas helt med 9")
"""

"""
#övning 6
ct = int(input("what time is it: "))
vakt = str(input("känner du vakten ja eller nej: "))

if vakt == "ja":
    print("free entrance")
elif ct <= 22 and ct >=  18:
    print("that will be 100kr")
elif ct > 22 or ct >= 0 and ct <= 3:
    print("that will be 250kr")
elif ct > 3 and ct < 18:
    print("we open at 18")
"""

#creates a 50%50 chance between 0 and 1
cc = randint (0,1)

#if cc is 1 it gets assigned left else it becomes rigth
if cc == 1:
    cc = "left"
else:
    cc = "right"

#asks user for a guess
user_Input = input("pick left or right: ")
if user_Input == cc:
    print("correct")
else:
    print("wrong")