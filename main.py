import random
import string


LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()"
COMBINED_LIST = list(LETTERS + NUMBERS + SYMBOLS)


def generate_password():
    random.shuffle(COMBINED_LIST)
    max_length = int(input("\nEnter your desired password length: "))
    password_list = []

    # add a random char from the COMBINED_LIST till the provided max password length has been reached
    for _ in range(max_length):
        password_list.append(random.choice(COMBINED_LIST))

    # shuffle the list and print out the password to the terminal
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Generated password: {password}")


while True:
    generate_password()
    if input("\nDo you want to generate another password? (y/n): ").casefold() != "y":
        print("\nExiting.")
        break