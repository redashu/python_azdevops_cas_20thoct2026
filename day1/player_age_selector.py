age = (10,20,30,11,45,77)
# this is infinite loop 
while True: 
    user_age = input("enter user age : ")

# here complete after age count 9 times terminate loop
valid_age = []
invalid_age = []
# implement for loop

for i in age: 
    print(f"currently checking {i}")
    if i >= 18:
        print(f"number {i} is valid for playing")
        valid_age.append(i)
    else : 
        print(f"number {i} is invalid for plahing")
        invalid_age.append(i)

# print final 
print("valid age numbers are ",valid_age)
print("invalid age numbers are ",invalid_age)