PASSWORD_MINIMUM_LENGTH = 7

password = input("Enter password: ")

while len(password) < PASSWORD_MINIMUM_LENGTH:
    print("Password must be at least {} characters long".format(PASSWORD_MINIMUM_LENGTH))
    password = input("Enter password: ")

print("*" * len(password))