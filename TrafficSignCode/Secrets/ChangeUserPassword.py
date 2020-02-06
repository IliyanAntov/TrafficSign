import hashlib
import os
import yaml

users = {}

with open("Users.yaml", 'r') as stream:
    try:
        loaded = yaml.safe_load(stream)
        for key, value in loaded.items():
            users[key] = value

        print("Existing users:")
        for i in users.keys():
            print(" -", i)
        print()
    except Exception as exc:
        print(exc)

print("Type --save-- to quit and save")
print()

username = input("Username: ")
while(username != "--save--"):
    newPassword = input("New password: ")

    salt = os.urandom(32) # Remember this
    passwordHash = hashlib.pbkdf2_hmac(
        'sha512', # The hash digest algorithm for HMAC
        newPassword.encode('utf-8'), # Convert the password to bytes
        salt, # Salt
        100000 # Iterations
    )

    users[username] = {
        'salt': salt,
        'password': passwordHash
    }

    print("OK")
    print()
    username = input("Username: ")


with open("Users.yaml", 'w', encoding='utf-8') as outfile:
    yaml.dump(users, outfile, default_flow_style=False, allow_unicode=True)