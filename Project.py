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
    pass
def choose_option():
    pass
def get_message():
    pass
def create_key(shift):
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
    return key
def encode(message,key):
    pass
def decode(message,key):
    pass