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
while True:
    choice = input("menu Type:\n1 -  add contact\n2 - view\n3 - search contact\n4 - delete\n5 - Exit\n:")
    
    if choice == "1":
        print("add menu choice")
    elif choice == "2":
        print("view menu choice")
    elif choice == "3":
        print("search Menu choice")
    elif choice == "4":
        print("delete Menu choice")
    elif choice == "5":
        break
    else:
        print("invalid Menu choice! please select a valid menu!!")

