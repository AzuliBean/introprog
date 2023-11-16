
#övning 4 a)&b)

user_Value = int(input("Input a value: "))

user_Choice = input("do you want the Square Root or Squared of your value? ")

if "Square Root" in user_Choice:
    square_Root = user_Value * 0.5
    print(square_Root)
elif "Squared" in user_Choice:
    squared = user_Value * user_Value
    print(squared)
print("hello world!")

"""
#övning 5

unknown_Type = 1 + 2.0 + 3 
print("Your data type is a: ")
print(type(unknown_Type))
"""

"""
#övning 6 

value = 6.2 
print("original value before converted to an int " + str(value))
print(int(value))
print(type(int(value)))
"""

"""
#övning 8 

celsius = int(input("input a temprature in in celsius to get it converted to farenheit: "))
farenheit = celsius * 9/5 + 32
print(str(celsius) + "*C in farenheit is " + str(farenheit) + "*F")
"""
