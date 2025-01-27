#This has proper time complexity than brutecodev2.py

import itertools
import string
import time

filename = "credentials.txt"
try:
    with open(filename, "r") as file:
        data = file.readlines()
        username = data[0].strip()
        password = data[1].strip()
except FileNotFoundError:
    print("The file does not exist. Make sure the file is in the same directory.")
    exit()
except IndexError:
    print("The file must contain the username on the first line and password on the second line.")
    exit()

def incremental_brute_force(password, char_set):
    print(f"Attempting to brute force a password of length {len(password)}...")
    start_time = time.time()
    cracked_password = ""

    for position in range(len(password)):
        for char in char_set:
            print(f"Trying character '{char}'")
            
            if password[position] == char:
                cracked_password += char
                print(f"'{char}'{position + 1}.{cracked_password}")
                break 
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Password cracked in {elapsed_time:.2f} seconds.")
    return cracked_password

character_set = string.ascii_letters + string.digits + string.punctuation

cracked_password = incremental_brute_force(password, character_set)

if cracked_password == password:
    print(f"\n\nPassword cracked successfully! \nUsername: {username}, Password: {cracked_password}")
else:
    print("Password could not be cracked.")
