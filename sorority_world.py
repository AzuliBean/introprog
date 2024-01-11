import sys

members = ['Augusta','Charmain','Billie','Mandy','Charlotte','Lesley']
likes = {'Augusta':['Charmain','Billie','Mandy','Charlotte','Lesley'],'Charmain':['Augusta','Mandy'],'Billie':['Augusta','Charmain','Lesley',],'Mandy':['Charlotte','Billie','Augusta'],'Lesley':['Billie']}
rooms_with = {'Augusta':'Charmain','Charmain':'Augusta','Billie':'Lesley','Lesley': 'Billie','Charlotte':'Mandy','Mandy':'Charlotte'}

def meny_val_ett(members):
    for x in members:
        print(x)

def meny_val_tva(members, likes):
    find = input("Vem är det du letar efter: ")

    if find not in members:
        print(f"{find} är inte medlem i föreningen")
        return
    
    liked = likes.get(find, [])

    if not liked:
        print(f"{find} gillar ingen")
    elif set(liked) == set(members) - {find}:
        print(f"{find} gillar alla.")
    else:
        print(f"{find} gillar: {', '.join(liked)}")

def meny_val_tre(members, rooms_with):
    find = input("Vem är det du letar efter: ")

    if find not in members:
        print(f"{find} är inte medlem i föreningen")
        return
    
    roommate = rooms_with.get(find, None)

    if roommate is not None:
        print(f"{find} delar rum med {roommate}")
    else:
        print(f"{find} delar inte rum med någon.")

def is_Integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def check_interval(data, low, high):
    if is_Integer(data):
        if int(data) in range(low, high + 1):
            return True
    return False

# Om det inte finns någon data: returnera False
def menu():
    print("Här är dina val:::")
    print("1: Lista alla medlemmar i föreningen")
    print("2: Vem tycker X om?")
    print("3: Vem delar X rum med?")
    print("4: Avsluta programmet")
        
def main_interaktion():
    slut = False
    while not slut:
        ok = False
        while not ok:
            menu()
            some_text = input("Mata in ett tal mellan 1-4: ")
            ok = check_interval(some_text,1,4)
            if not ok:
                print("Du måste mata in något mellan 1 och 4")
                break
            ett_heltal = int(some_text)
            if ett_heltal == 4:
                print("Hejdå")
                slut = True
                break
            if ett_heltal == 3:
                meny_val_tre(members,rooms_with)
            if ett_heltal == 2:
                meny_val_tva(members,likes)
            if ett_heltal ==1:
                meny_val_ett(members)
    
# Nedanstående är en vanlig konstruktion för att köra main_interaktion()-funktionen vid uppstart.
# Ni behöver inte förstå hur denna kod funkar, bara att programmet startar med main_interaktion().
if __name__ == "__main__":
    main_interaktion()




    
