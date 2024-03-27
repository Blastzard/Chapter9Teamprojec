import string
def main():
    #Team project
    #accepts no arguments
    #calls all functions
    shift=get_shift()
    message=get_message()
    choice=choose_option()
    key=create_key(shift)
    if choice==False:
        message=decode(message,key)
        print("Here is your decoded message")
        print(message)
    elif choice==True:
        message=encode(message,key)
        print("Here is your encoded message")
        print(message)
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
        
    return shift
def get_message():
    #prompts user to enter a message to encode or decode
    #returns the message
    
    message = input("Enter a message to encode or decode: ")
    
    message1=message.replace(""," ")
        
    while message1.isalpha() == False:
        
        message = input("Enter a message to encode or decode: ")
        
        message1=message.replace(""," ")
    
    return message
        

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

def create_key(shift):
    #team project
    #create key
    #accepts integar
    uletters=string.ascii_uppercase
    letters=string.ascii_lowercase
    key=dict()
    index=0
    index1=0
    for x in letters:
        index=index1+shift
        if index>25:
            index=(26-index)*-1
        key[x]=letters[index]
        index1+=1
        index=0
    index1=0
    index=0
    for x in uletters:
        index=index1+shift
        if index>25:
            index=(26-index)*-1
        key[x]=uletters[index]
        index1+=1
        index=0
    key[" "]=" "
    return key
  
def encode(message, key):
    print("Here is your encoded message: ")
    
    for x in message:
        letter1 = key[x]
        letter = letter + letter1
    
    return letter
    
def decode(message,key):
    #teamproject
    #accept string and list
    #decodes a message
    for key, value in key.items():
            index+=1
            codes[value]=key
    for x in message:
        letter1=key[x]
        letter=letter+letter1
    return letter