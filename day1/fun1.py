# asking user input untill q or quit is being typed
import time 
user_input_list = []
# define a function to take user input 
def u_input():
    while True: 
        user_input = input("enter number : ")
        if user_input == 'q' or user_input == 'quit':
            break
        else :
            user_input_list.append(int(user_input)) 

    print(user_input_list)

# # call function 
# u_input()

## creating sum function 
def adding():
# calling input 
    for i in u_input():
        print(i)
        time.sleep(1)


# calling add 
adding()

