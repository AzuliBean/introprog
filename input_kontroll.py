import sys

#creates the function check_datatype
def check_datatype(data, datatype):
    #these are a set of help functions that checks if the data that is given is a int,float,str using isinstance 
    def is_Integer(data):
        #if the object "data" is a integer the it will return true if not it will return false
        return isinstance(data, int)

    def is_Float(data):
        #if the object "data" is a float the it will return true if not it will return false
        return isinstance(data, float)

    def is_Text(data):
        #if the object "data" is a string the it will return true if not it will return false
        return isinstance(data, str)

    #if statement that checks if the input is is both assigned "I" as well as is_Integer and if that is true then it will return True
    if datatype == "I" and is_Integer(int(data)):
        return True
    #if statement that checks if the input is is both assigned "F" as well as is_Float and if that is true then it will return True
    elif datatype == "F" and is_Float(float(data)):
        return True
    #if statement that checks if the input is is both assigned "T" as well as is_Text and if that is true then it will return True
    elif datatype == "T" and is_Text(data):
        return True
    #if none of these if statements are true then it will exit the application 
    else:
        exit()

def main_interaktion():
    while True:
        print ("1: Kontrollera heltal: ")
        print ("2: Mata in ett flyttal: ")
        print ("3: Mata in text: ")
        print ("4: Avbryt programmet")

        svar = input("\nMata in ett alternativ: ")
        if svar == '1':
            tal = input("\nMata in ett heltal: ")
            if not check_datatype(tal,'I'):
                print("Det var inte ett heltal")
            else:
                print("Input OK")
        elif svar == '2':
            tal = input("\nMata in ett flyttal: ")
            if not check_datatype(tal,'F'):
                print("Det var inte ett flyttal")
            else:
                print("Input OK")
        elif svar == '3':
            tal = input("\nMata in lite text: ")
            if not check_datatype(tal,'T'):
                print("Du måste mata in något")
            else:
                print("Input OK")
        elif svar == '4':
            break
        else:
            print("Felaktigt val")
            


# Nedanstående är en vanlig konstruktion för att köra main_interaktion()-funktionen vid uppstart.
# Ni behöver inte förstå hur denna kod funkar, bara att programmet startar med main_interaktion().
if __name__ == "__main__":
    main_interaktion()
    
