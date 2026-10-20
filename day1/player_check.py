# enter player name 
player_name = input("enter player name : ")
player_age = input("enter player age : ")

# print("My player name is ",player_name)
# print("My player Age is ",player_age)

# using format option in print 

# print(f"My player name is {player_name}")
# print(f"My player Age is {player_age}")

# using .format function 

print("My player name is {}".format(player_name))

print("My player name is {0} and player age is {1}".format(player_name,player_age))

# if & else 

if int(player_age) < 18 :
    print(f"Player {player_name} not Eligible")

elif int(player_age) <= 20 :
    print(f"player {player_name} required age verification")

elif int(player_age) > 20 and int(player_age) <= 35:
    print(f"player {player_name} best fit ")

else : 
    print(f"Player {player_name} is less preferable but still can play")