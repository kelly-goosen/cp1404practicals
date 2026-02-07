"""Password length checker that prints in asterisks"""

PASSWORD_MINIMUM_LENGTH = 7

def main():
    """Ask for a password and print asterisks (* length) if valid."""
    password = get_password()
    print_astericks(password)


def print_astericks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < PASSWORD_MINIMUM_LENGTH:
        print("Password must be at least {} characters long".format(PASSWORD_MINIMUM_LENGTH))
        password = input("Enter password: ")
    return password


main()