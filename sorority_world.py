import sys

members = ['Augusta','Charmain','Billie','Mandy','Charlotte','Lesley']
likes = {'Augusta':['Charmain','Billie','Mandy','Charlotte','Lesley'],'Charmain':['Augusta','Mandy'],'Billie':['Augusta','Charmain','Lesley',],'Mandy':['Charlotte','Billie','Augusta'],'Lesley':['Billie']}
rooms_with = {'Augusta':'Charmain','Charmain':'Augusta','Billie':'Lesley','Lesley': 'Billie','Charlotte':'Mandy','Mandy':'Charlotte'}





def meny_val_ett(members):
    for member in members:
        print(members)

def meny_val_tva(members, likes):
    find = input("Who is it that you're looking for: ")

    if find not in members:
        print("f{find} is not a member of the association")
        return
    
    liked = likes.get(find, [])

    if not liked:
        print(f"{find} doesn't like anyone")
    elif set(liked) == set(members) - {find}:
        print(f"{find} likes everyone(except themselves).")
    else:
        print(f"{find} likes: {', '.join(liked)}")

def meny_val_tre(members, rooms_with):
    find = input("Who is it that you're looking for")

    if find not in members:
        print("f{find} is not a member of the association")
        return
    
    roommate = rooms_with.get(find, None)

    if roommate is not None:
        print(f"{find} shares a room with {roommate}")
    else:
        print(f"{find} does not share a room with anyone.")



def check_datatype(data, datatype):
    
    def is_Integer(data):
        # if the object "data" is an integer, then return True; otherwise, return False
        return isinstance(data, int)

    def is_Float(data):
        return isinstance(data, float)

    def is_Text(data):
        return isinstance(data, str)

    if not datatype in "IFT":
        sys.exit(f"Error processing data. Expected a: {datatype} but got : {data}")

    # tests if you get an error
    try:
        if datatype == "I" and is_Integer(int(data)):
            return True

        elif datatype == "F" and is_Float(float(data)):
            return True

        elif datatype == "T" and is_Text(data):
            return True
    # if there is an error, then run the code under 
    except:
        return False

# The check_interval function from the first code snippet remains unchanged
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




    
