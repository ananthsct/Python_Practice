import re

def is_strong_password(password, name):
    # Check length condition
    if not (6 <= len(password) <= 20):
        return False

    # Check for at least one lowercase, one uppercase, and one digit
    if not (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)):
        return False

    # Check for at least one special character (using regex)
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # Check for repeating characters in a row
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return False

    # Check if the first 4 characters of the name are in the password
    if name[:4] in password:
        return False

    # Password meets all conditions
    return True

# Test cases
name = "John"
passwords = ["Abc123!John", "abc123John", "Jo@hgadfgn123", "123456", "Baaba0", "Baaabb0", "Abc12345"]
for password in passwords:
    if is_strong_password(password, name):
        print(f"'{password}' is a strong password.")
    else:
        print(f"'{password}' is a weak password.")
