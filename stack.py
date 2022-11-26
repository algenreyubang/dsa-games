def stack():
    print("take a  lokk of this set of number ")
    print('0')
    print('2')
    print('1')
    print('4')
    print('3')
    print('5')
    print("your task is to stack them in corect order form 0 to 5")
     
    stack_input = input()

    if stack_input == "0,1,2,3,4,5":
        print("well played")
    elif stack_input != input():
        stack()
        print("try again")
        
    else: print("error")
    
        
        
    
        
        
stack()
