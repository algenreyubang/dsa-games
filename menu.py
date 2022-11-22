def start():
 return " your in start"

# def retuner():
    
#     selection_input = str(input())
#     if selection_input == '0':
#         print(menu())
#     else: 
#         print("options\n[1]  \n[0] return to the options ")
#         selection_input == '0'

def option():
    print("options\n[1]something  \n[0] return to options ")
    
    selection_input = str(input())
    if selection_input == '2':
        print("your in the options")
    elif selection_input == '1':
        print("konwari may volume, tas adjust grapics at brightness")  
        print(menu())
        
    elif selection_input == '0':
        print(menu())    

    

def menu():
    print("options \n[1] start \n[2] settings\n[3] how to play\n[4] exit")
   
    selection_input = str(input())
    if selection_input == '1':
        print(start())
        print(option())
    elif selection_input == '2':
        print(option())
    elif selection_input == '3':
        print("you entered how to play")   
        print(option()) 
    else:
     selection_input == '4'
     exit
menu()            