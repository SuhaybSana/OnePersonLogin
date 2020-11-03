import pickle
import os
import sys
import time

print()
file = ""

def new_account():
    new_username = input("Please create a username: ")
    new_password = input("Please create a password: ")

    pickle.dump(new_username, open("Username.dat", "wb"))
    pickle.dump(new_password, open("Password.dat", "wb"))

    print("Account Created")
    file = open("Accounts.txt", "w+") 
    file.write("True")

def close():
    print("Closing program...")
    from time import sleep
    sleep(0.5)
    print("Program closed")
    sys.exit()

# User Input / Login / Create Account

print("Do you want to sign up or login")
print("\n"+ "*"*15)
print("Commands: ")
print("1 = Sign up")
print("2 = Login")
print("3 = Quit")
print("\n"+ "*"*15)
input_ = int(input())

if input_ == 1: 
    new_account()
    print("Welcome!! this is your account, it is currently empty")

if input_ == 2:
    txt = open("Accounts.txt", "r")
    if "True" not in txt:
        new_account()
    else:
        print("You have an account!")

    username = input("Enter you username: ")
    use = pickle.load(open("Username.dat", "rb"))

    while username not in use:
        username = input("Enter a valid username: ")
        
        if username == "3":
            close()

    password = input("Enter your password: ")
    pas = pickle.load(open("Password.dat", "rb"))

    while password not in pas:
        password = input("Enter a valid password: ")
    
        if password == "3":
            close()
    
    print("Welcome back!! this is your account, it is currently empty")

if input_ == 3:
    close()
