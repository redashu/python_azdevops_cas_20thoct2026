# taking user input as their names max input as 4 
user_names = []


while len(user_names) < 4:
    name=input("enter user name:  ")
    user_names.append(name) 

# printing all the names 
print(user_names)

# creating function to keep only those names whosoever having s char
user_new = []
def check_names():
    for  i in user_names:
        if 's' in i:
            user_new.append(i)
        else:
            print(f"username {i} not in category")
    return user_new

# calling function 
check_names()


