import sys


def check_datatype(data, datatype):
    
    def is_Integer(data):
        #if the object "data" is a integer the it will return true if not it will return false
        return isinstance(data, int)

    def is_Float(data):
        
        return isinstance(data, float)

    def is_Text(data):
        
        return isinstance(data, str)
    
    if not datatype in "IFT":
        sys.exit(f"Error processing data. Expected a: {datatype} but got : {data}")
    #tests if you get a a error
    try:
       
        if datatype == "I" and is_Integer(int(data)):
            return True
        
        elif datatype == "F" and is_Float(float(data)):
            return True

        elif datatype == "T" and is_Text(data):
            return True
    #if there is a error then run the code under 
    except:
       return False


        

        

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
    
