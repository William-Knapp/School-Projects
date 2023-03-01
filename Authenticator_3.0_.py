#!/usr/bin/env python
#Made with assistance from ChatGPT: https://chat.openai.com/chat

#This program is a simple authentication application that allows users to create user accounts and authenticate user input against stored credentials
#It stores the password as a SHA256 hash for security purposes, has an adjustable number of max attempts and lockout duration, and checks that entered passwords
#are at least 8 characters long, have at least one upper case character and at least one lower case character, a number, and a special character as defined in the `chars`
#array below. There are two classes: `User`, which stores a user's information (including hashed password), and `Authenticator`, which performs authentication functions and 
#handles the creation of `User` objects, which are stored in a dictionary.

import hashlib
import time
import math

#Stores username and hashed password for use in `Authenticator`
class User:

    #constructor with username and password taken from `Authenticator`
    #Includes hashing algorithm for security purposes
    def __init__(self, username, password):
        self.username = username
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.failed_attempts = 0
        self.locked_until = 0
        self.password_hash_history = []
        self.password_hash_history.append(self.password_hash)
    
    #checks if stored password hash matches password given by `Authenticator`
    def check_password(self, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return password_hash == self.password_hash

#Main class. Checks password requirements, keeps a dictionary of `User` objects, and performs authentication functions.
class Authenticator:

    #Constructor. Creates dictionary to store `User` objects and defines maximum attempts and lockout duration.
    def __init__(self):
        self.users = {}
        self.max_attempts = 3
        self.lockout_duration = 300
    
    #Checks entered password to ensure it meets requirements. (upper, lower, digit, >8 characters, has a special character)
    def check_requirements(self, username, password):
        if (password.upper() == password):
            return False
        elif (password.lower() == password):
            return False
        elif(not any(i.isdigit() for i in password)):
            return False
        elif(len(password) < 8):
            return False
        elif(not self.has_special(password)):
            return False
        elif(username in password):
            return False
        return True

    #Called by check_requirements() to check if the password has a special character.
    #Can modify what is defined as a special character by adding/removing values from the `chars` array.
    def has_special(self, password):
        chars = ['!', '@', '#', '$', '%', '^', '&', '*', '~', '`', '(', ')', '-', '+']
        for c in password:
            if (c in chars):
                return True
        return False

    #Creates `User` object with given username and password and stores in dictionary initialized in __init__
    def add_user(self, username, password):
        if username in self.users:
            print("User already exists\n")
            return False
        else:
            u = User(username, password)
            self.users[username] = u
            return True
    
    #Authenticates user by given username and password. Has a lockout feature to prevent brute force attacks, implemented by taking the system time
    #when the user is first locked out, and then adding the specified `lockout_duration` to it.
    def authenticate(self, username, password):

        if username in self.users:
            u = self.users[username] #allows `u` to be used in place of `self.users[username]`
            if u.locked_until > time.time(): #checks if the user is already locked
                print("\nAccount is locked. Try again in", math.ceil((u.locked_until - time.time())/60), "minute(s).")
                return False
            elif u.check_password(password):
                u.failed_attempts = 0
                return True
            else:
                u.failed_attempts += 1
                if u.failed_attempts >= self.max_attempts:
                    u.locked_until = time.time() + self.lockout_duration #locks account by checking time and adding specified duration
                    u.failed_attempts = 0
                    print("\nToo many failed attempts. Account will be locked for", int(self.lockout_duration/60), "minutes.")
        return False
    
    def update_password(self, username, password):
        if username in self.users:
            u = self.users[username]
            if self.check_requirements(username, password):
                new_password_hash = hashlib.sha256(password.encode()).hexdigest()
            else:
                print("\nPassword does not meet the requirements. Passwords must contain:\n1 upper case letter, 1 lowercase letter, 1 number, and 1 special character.\nPasswords must also be at least 8 characters long,\nand must not contain your username.\n")
                return False
            if new_password_hash in u.password_hash_history:
                print("\nPassword must be different from last 3 passwords.")
                return False
            u.password_hash = new_password_hash
            u.password_hash_history.insert(0, u.password_hash)
            if len(u.password_hash_history) > 3:
                u.password_hash_history.pop(3)
            return True
        return False


#main function. Has a loop that will continue until the user enters "3". Mostly handles menu items and print statements.

def main():
    print()
    auth = Authenticator()
    while True:
        print("*** Main Menu ***")
        print("1. Add user")
        print("2. Authenticate")
        print("3. Update password")
        print("4. Quit")
        print()
        choice = input("Enter choice: ")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter either 1, 2, 3 or 4.\n")
            continue
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter a password: ")
            print()
            while not (auth.check_requirements(username, password)):
                print("\nPassword does not meet the requirements. Passwords must contain:\n1 upper case letter, 1 lowercase letter, 1 number, and 1 special character.\nPasswords must also be at least 8 characters long,\nand must not contain your username.\n\nTry again.")
                password = input("Enter password: ")
            if auth.add_user(username, password):
                print("User added successfully\n")
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if auth.authenticate(username, password):
                print("\nAccess granted\n")
            else:
                print("\nAccess denied\n")
        elif choice == "3":
            username = input("Enter username: ")
            password = input("Enter current password: ")
            if not (auth.authenticate(username, password)):
                print("\nAuthentication failed.\n")
            else:
                password = input("Enter new password: ")
                if auth.update_password(username, password):
                    print("\nPassword updated successfully.\n")
                else:
                    print("Password update failed.\n")
        else:
            break

if __name__ == "__main__":
    main()