import itertools

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


def brute_force_password(password):
    max_length = len(password)  
    print(f"Attempting to brute force password of length {max_length}...")
    
    for length in range(1, max_length + 1):  
        for guess in itertools.product("0123456789", repeat=length):
            attempt = ''.join(guess)
            print(f"Trying: {attempt}")  
            if attempt == password:
                return attempt

# Call the brute force function
cracked_password = brute_force_password(password)


