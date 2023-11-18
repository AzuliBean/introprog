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

"""
#övning 10
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
"""

"""
#övning 11
value_One = int(input("input your value: "))
value_Two = int(input("input your value you want to devided with: "))

if value_Two == 0:
    print("you cannot divide with 0")
elif value_One % value_Two == 0:
    print("yes ", value_One, "and", value_Two, "are able to divide without decimals left behind")
else: 
    print("no ", value_One, "and", value_Two, "aren't able to divide without decimals left behind")
"""

"""
#övning 12
timme = int(input('Ange timma: ')) 
minut = int(input('Ange minut: ')) 
plats = input('Ange plats: ') 
tidsskillnad = int(input('Ange tidskillnad i hela timmar: ')) 

# räkna ut vilken hel timme du hamnar på 
timme_annan_tidszon = timme + tidsskillnad

# kontrollera så att ny hel timme inte blir för stor eller negativ
if timme_annan_tidszon >= 24:    
    timme_annan_tidszon = timme_annan_tidszon - 24 
elif timme_annan_tidszon < 0:     
    timme_annan_tidszon = timme_annan_tidszon + 24

tid_annan_tidszon = str(timme_annan_tidszon) + ":" + str(minut) 
                                         
print("Klockan är nu ", tid_annan_tidszon, "i", plats)
"""

"""
#övning 13
rain = input("is it raining yes or no? ")
R = True if rain == "yes" else False
wind = input("is it windy yes or no? ")
W = True if wind == "yes" else False

if (R == True and W == False):
    print("The presumption isn't correct")
else:
    print("The presumption is correct")
"""

"""
#övning 14
user_Input = int(input("what length do you want your paper to be in mm: "))

if user_Input <= 148:
    print("A6")
elif user_Input <= 210:
    print("A5")
elif user_Input <= 297:
    print("A4")
elif user_Input <= 420:
    print("A3")
elif user_Input <= 594:
    print("A2")
else:
    print("sorry there is no paper format that is big enough")
"""

"""
#övning 15
user_Answer_A = str.lower(input("do you want to Cooperate or do you want to Betray: "))
user_A = True if user_Answer_A == "cooperate" else False

user_Answer_B = str.lower(input("do you want to Cooperate or do you want to Betray: "))
user_B = True if user_Answer_B == "cooperate" else False

if user_A and user_B:
    print("both players got 2 points ")
elif user_A and not user_B:
    print("User B betrayed User A and got all the points instead")
elif user_B and not user_A:
    print("User A betrayed User B and got all the points instead")
else:
    print("Both players tried to betray eachother and no one ended up getting points")
"""

"""
#övning 16
user_Choice = str.lower(input("Äntligen är du ute i naturen! Du kommer till ett vägskäl. \nVälj att: \nA: gå mot den mystiska skogen eller B: gå mot havets vägljud? \nVad väljer du:  "))

if user_Choice == "a":
    user_Choice = str.lower(input("\nEn gigantisk orm dyker upp! \nVälj att \nA: Springa eller B: Spela död \nVad väljer du:  "))

    if user_Choice == "a":
        print("\nDu är chanslös och ångrar bittert att du lämnat samhället")
    else: 
        print("\nOrmen äter en get som följt dig istället och du hittar blåbär")

elif user_Choice == "b":
    user_Choice = str.lower(input("\nHavet suger och du blir hungrig. \nVälj att \nA: äta en snigel eller B: Försök fiska \nVad väljer du: "))

    if user_Choice == "a":
        print("\nDu möter döden och utmanar döden till schack")
    else:
        print("\nDu får bottennapp, det är ätlig tång med nyttiga vitaminer")
"""