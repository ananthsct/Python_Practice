import getpass
import os

# Prompt the user for a password
password = getpass.getpass("Enter your password: ")

# Store the password in a .env file
with open(r'practice\facebookLogin\.env', 'w') as env_file:
    env_file.write(f'PASSWORD={password}')

print("Password saved to .env file.")
