import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    if min_length < 1:
        min_length = 1

    
    password = []
    if numbers:
        password.append(random.choice(digits))
    if special_characters:
        password.append(random.choice(special))
    
    
    while len(password) < min_length:
        password.append(random.choice(characters))

    
    random.shuffle(password)

    return ''.join(password)


# User input
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").strip().lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").strip().lower() == "y"

# Generate and display the password
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
