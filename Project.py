def main():
    pass

def get_shift():
    #prompts user for shift value
    #returns value as string
    #validates for integers 1-25 inclusive
    
    shift = input("Enter a shift value from 1 to 25: ")
    
    while shift.isdigit() == False:
        shift = input("Enter a valid shift value from 1 to 25: ")
    
    shift = int(shift)
    
    while shift < 1 or shift > 25:
        shift = input("Enter a valid shift value from 1 to 25: ")
        while shift.isdigit() == False:
            shift = input("Enter a valid shift value from 1 to 25: ")
        shift = int(shift)
        
    return str(shift)
        

def choose_option():
    #prompt user for choice to decode or encode
    #return true if chosen encode and False if chosen decode
    eChoice = 1
    dChoice = 2
    
    print("1. Encode")
    print("2. Decode")
    
    choice = input("Enter 1 or 2 to encode or decode: ")
    
    while choice.isdigit() == False:
        choice = input("Enter a valid input (1 or 2): ")
    
    choice = int(choice)
    
    
    while choice < 1 or choice > 2:
        choice = input("Enter a valid input (1 or 2): ")
        while choice.isdigit() == False:
            choice = input("Enter a valid input (1 or 2): ")
        choice = int(choice)
    
    if choice == 1:
        return True
    
    elif choice == 2:
        return False

def get_message():
    pass

def create_key():
    pass

def encode(message,key):
    pass

def decode(message,key):
    pass