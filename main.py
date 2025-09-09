"""
loop: while loop 
contacts ={"adam": {" phone number": 08012345678, email :"adam@gmail.com"},
"eve": {" phone number": 08012345678, email :"alice@gmail.com"}
}
contacts ={}
menus:
1 = add contact 
2 = view contact

"""
contact_book = {}

def addcontact():
    contact_name = input("enter contact name : ")

    
    if contact_name not in contact_book:
        contact_phone = input("enter contact phone number: ")
        contact_email = input("enter contact email:")
        contact_details = dict(phone_numer = contact_phone, email = contact_email)
        contact_book[contact_name] = contact_details
        print(contact_details)
    else:
        print("name already exists, kindly choose another name.")

def viewcontact():
    for key,value in contact_book.items():
        print(f"{key}:")
        for key, value in value.items():
            print(F"{key} : {value}")
        print("=====================================")

def seachcontact():
    search_name = input("enter the contact name to search: ")
    if search_name in contact_book:
    
        #filter
        filtered = {k: v for k, v in contact_book.keys() if k == search_name}
        print(filtered)      
def deletecontact():
    delete_name = input ("enter contact name to be detected: ")
    
    if delete_name in contact_book:
        del delete_name
        print(f"{delete_name} is sucessfully deleted from your contact book !")
    else:
        print(f"{delete_name} does not exists in the contact book")
while True:
    choice = input("menu Type:\n1 -  add contact\n2 - view\n3 - search contact\n4 - delete\n5 - Exit\n:")
    
    if choice == "1":
        addcontact()
    elif choice == "2":
        viewcontact
    elif choice == "3":
        seachcontact()
    elif choice == "4":
        print("delete Menu choice")
    elif choice == "5":
        break
    else:
        print("invalid Menu choice! please select a valid menu!!")
        

