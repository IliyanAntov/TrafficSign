import hashlib
import os
import yaml

users = {}  # Available users dictionary

# Open the Users.yaml file as a readable stream
with open("Users.yaml", "r") as stream:
    try:
        # Convert the contents of the file to a python object
        loaded = yaml.safe_load(stream)
        # Add every loaded entry to the users dictionary
        for key, value in loaded.items():
            users[key] = value

        # Print every available username
        print("Existing users:")
        for i in users.keys():
            print(" -", i)
        print()
    # File loading failed
    except yaml.YAMLError as exc:
        print(exc)

print("Type --save-- to quit and save")
print()

# Read username
username = input("Username: ")
# Read until the user enters the --save-- command
while username != "--save--":
    # Read the new password for the user
    newPassword = input("New password: ")

    # Generate a truly random 32 byte salt
    salt = os.urandom(32)

    # Generate the password hash using pbkdf2
    passwordHash = hashlib.pbkdf2_hmac(
        "sha512",  # Hash algorithm
        newPassword.encode("utf-8"),  # Convert the password to bytes
        salt,  # Salt
        100000,  # Iterations of the hash algorithm
    )

    # Store the user's new salt and password hash
    users[username] = {"salt": salt, "password": passwordHash}

    print("OK")
    print()
    # Read another username
    username = input("Username: ")

# Open the Users.yaml file as a writeable stream
with open("Users.yaml", "w", encoding="utf-8") as outfile:
    # Dump the contents of the users dictionary to the file in utf-8 format
    yaml.dump(
        users,  # Users dictionary
        outfile,  # Output stream
        default_flow_style=False,  # Save collection in block style
        allow_unicode=True,  # Save characters in unicode instead of binary
    )
