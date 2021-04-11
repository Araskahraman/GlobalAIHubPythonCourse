# -*- coding: utf-8 -*-



username1 =input("Please enter your username")

password1= input("Please enter your password")


username = "Aras"
password ="142536"

if (username != username1 and password == password1):
    print("Your username is invalid")
elif (username == username1 and password != password1):
    print("Your password is invalid")
elif (username != username1 and password != password1):
    print("Your username and password are invalid")
else:
    print("You are logged in!")
    
    
#%% 
all_data = {"Aras" : "142536",
             "Evrim": "172839",
             "Mert" : "123456",
             "Gamze": "357159"}

getting_username = input("Please enter your username")
getting_password = input("Please enter your password")

all_usernames = list(all_data.keys())
all_passwords = list(all_data.values())

if (getting_username not in all_usernames and getting_password in all_passwords):
    print("Please try again")
elif (getting_username in all_usernames and getting_password not in all_passwords):
    print("Please try again")
elif (getting_username not in all_usernames and getting_password not in all_passwords):
    print("Your username and password are invalid")
else:
    print("You are logged in!")
    
