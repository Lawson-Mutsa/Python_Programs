# Importing required modules, packages and libraries
import string
import random

# Main Function
def main():
    while True:
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Welcome to the Password Generator Application")
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print()

        # Selecting an option between auto generate password and customize password
        user_option = int(input(
            "How would you like to generate your password?\n"
            "1. Customize password \n"
            "2. Auto-generate password \n"
        ))

        # Customize password
        if user_option == 1:
            customize_password()
            break

        # Auto generate password
        elif user_option == 2:
            auto_generate_password()
            break

        # Invalid option
        else:
            print("Select option 1 or 2")

# Asking the user for the custom password number options
def customize_password_input():
    lowercase_letters_options = int(input("Number of lowercase letters: "))
    uppercase_letters_options = int(input("Number of uppercase letters: "))
    numbers_options = int(input("Number of digits to be added to password: "))
    special_symbols_options = int(input("Number of special symbols: "))
    return  lowercase_letters_options, uppercase_letters_options, numbers_options, special_symbols_options

# Generating the custom password based on user input
def customize_password():
    lowercase_option, uppercase_option, numbers_option, special_symbols_option = customize_password_input()
    small_letters = list(string.ascii_lowercase)
    capital_letters = list(string.ascii_uppercase)
    numbers = list(string.digits)
    special_symbols = list(string.punctuation)

    part_password1 = random.sample(small_letters,k=lowercase_option)
    part_password2 = random.sample(capital_letters,k=uppercase_option)
    part_password3 = random.sample(numbers,k=numbers_option)
    part_password4 = random.sample(special_symbols,k=special_symbols_option)
    password = part_password1 + part_password2 + part_password3 + part_password4
    random.shuffle(password)

    print()
    print(f"Your custom password is {''.join(password)}")

# Generating random numbers
def random_numbers():
    lowercase_letters_options = random.randint(1,26)
    uppercase_letters_options = random.randint(1,26)
    numbers_options = random.randint(1,10)
    special_symbols_options = random.randint(1,32)
    return  lowercase_letters_options, uppercase_letters_options, numbers_options, special_symbols_options

# Generating password based on random numbers
def auto_generate_password():
    lowercase_option, uppercase_option, numbers_option, special_symbols_option = random_numbers()
    small_letters = list(string.ascii_lowercase)
    capital_letters = list(string.ascii_uppercase)
    numbers = list(string.digits)
    special_symbols = list(string.punctuation)

    part_password1 = random.sample(small_letters,k=lowercase_option)
    part_password2 = random.sample(capital_letters,k=uppercase_option)
    part_password3 = random.sample(numbers,k=numbers_option)
    part_password4 = random.sample(special_symbols,k=special_symbols_option)
    password = part_password1 + part_password2 + part_password3 + part_password4
    random.shuffle(password)

    print()
    print(f"Your auto generated password is {''.join(password)}")

# Calling main function
main()