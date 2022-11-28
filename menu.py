
 
def retuner():
    print("if you want to go back to the menu press 0 but your game will be reset")
    print("options\n[1] dadada  \n[0] return to the options ")
    selection_input = str(input())
   
    if selection_input == '0':
        print(menu())
    else: 
        selection_input == '1'
        print("datadta")

 
def secondretuner():
    print("if you want to go back to the menu press 0")
    print("options\n[1] dadada  \n[0] return to the options ")
    selection_input = str(input())
   
    if selection_input == '0':
        print(menu())
    else: 
        selection_input == '1'
        print("datadta")       

def setthings():
    print("sethings \n[0] return to options  \n[1] something   \n[2] enter to options ")
    
    selection_input = str(input())
    if selection_input == '2':
        print("your in the options")
        print(secondretuner())
    elif selection_input == '1':
        print("konwari may volume, tas adjust grapics at brightness")  
        print(secondretuner())
        
    elif selection_input == '0':
        print(secondretuner())    

    

def menu():
    print("menu \n[1] start \n[2] settings\n[3] how to play\n[4] exit")
   
    selection_input = str(input())
    if selection_input == '1':
        from stack import stack
        stack()
        print(retuner())
        retuner()
    elif selection_input == '2':
        print(setthings())
    elif selection_input == '3':
        print("you entered how to play") 
        secondretuner()      
    elif selection_input == '4':
        exit()
    else: 
        print("choto erroi, yamete kudasai oni-chan!! ")
        print("FBI open up onichan!! ")
        exit()
menu()            