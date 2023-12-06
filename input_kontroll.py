import sys

def check_datatype(data, datatype):
    def is_Integer(data):
        return isinstance(data, int)

    def is_Float(data):
        return isinstance(data, float)

    def is_Text(data):
        return isinstance(data, str)

    if datatype == "I" and is_Integer(int(data)):
        return True
    elif datatype == "F" and is_Float(data):
        return True
    elif datatype == "T" and is_Text(data):
        return True
    else:
        print(f"Error: This data type is not valid {datatype}")
        sys.exit()

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
    
