print("welcome to our game project")
print("main menu")
# register
def register():
    db = open("database.txt" ,"r")
    Username = input("Create username;")
    Password = input("Create password;")
    Password1 = input("Confirm password;")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))    
    #print(data)
    if Password != Password1:
        print("passwords dont match, restart")
        register()
        
    else:
        if len(Password)<=7:
            print("password too weak, restart")
            register()
        elif Username in d:
            print("username exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write(Username+", "+Password+"\n")
            print("Success")



def access():
    db = open("database.txt" ,"r")
    Username = input("enter your username;  ")
    Password = input("enter your password;  ")

    if not len(Username or Password)<1:
        d = []
        f = []
        for i in db:
             a,b = i.split(", ")
             b = b.strip()
             d.append(a)
             f.append(b)
        data = dict(zip(d, f))   

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        
                        print("login success")
                        print("hi,", Username)
                        from menu import menu
                        menu
                    else:
                        print("Password or username incorrect") 
                except:
                    print("incorrect password or username")   
            else:
                print("username and password doesnt exist")
        except:
            print("username and password doesnt exist") 
    else:
        print("please enter a value")

# home
def home(option=None):
    option = input ("login:  |  register:  |  log out: ")
    if option == "login":
        access()
    elif option == "register":
        register()
    elif option == "log out":
        return True    
    else:
        print("please enter an option")   
        
home()  
# from menu import menu
# menu


















# from menu import menu
# menu
# def menu():
#     print("[1] start the game")
#     print("[2] Settings")
#     print("[3] How to play")
#     print("[4] back")

# def option1():
#     print( " welcome " )
    
# def option2():
#     print("welcome to settings") 
# def option3():  
#     print("how to play??")  
# def option4():    
#     print("back??")    
# menu()
# option = int(input ("enter your option:  "))
    
# while option !=0:
#     if option == 1:
#         option1()
#         print("welcome to wild rift")
#     elif option == 2:
#         option2()     
#     elif option == 3:
#         option3()     
#     elif option == 4:
#         option4()    
#     else:
#         print("invalid option")
#         print("please enter option")
#     menu()
#     option = int(input ("enter your option: "))

# print()

















# sample menu
# def menu():
#     # print(" 1.start the game, \n 2.Settings, \n 3.How to play, \n 4.Back ")
#     # option = input
#     # # try:
#     # if option == "1":
#     #     print("welcome to wild rift")
#     #     menu()
#     # if option == "2":
#     #     print("wellcome to settings")
#     #     menu()     
#     # if option == "3":
#     #     print("wellcome to how to play")
#     #     menu() 
#     # if option == "4":
#     #     print("back ")
#     #     menu() 
#     # else:
#     #      print("please ")   
#     # # except:
#     #     # print("please enter number 1-4")   
# menu()           