import string
import secrets


def generate_password(length: int):
    # if length % 3 != 0:
    #     raise ValueError("Password length must be a multiple of 3.")

    num_letters = length // 3
    num_digits = length // 3
    num_punctuation = length - (num_letters + num_digits)

    # Define character sets
    letter_chars = string.ascii_letters
    digit_chars = string.digits
    punctuation_chars = string.punctuation

    # Generate random characters from each set
    chars = [secrets.choice(letter_chars) for _ in range(num_letters)]
    print(chars)
    letters = ''.join(secrets.choice(letter_chars) for _ in range(num_letters))
    digits = ''.join(secrets.choice(digit_chars) for _ in range(num_digits))
    punctuation = ''.join(secrets.choice(punctuation_chars) for _ in range(num_punctuation))

    # Shuffle the characters
    combined_chars = list(letters + digits + punctuation)
    print(combined_chars)
    secrets.SystemRandom().shuffle(combined_chars)

    # Convert the shuffled characters to a string
    password = ''.join(combined_chars)

    print(f'Generated Password: {password}')

# Example: Generate a password with 9 characters (3 letters, 3 digits, 3 punctuation)
generate_password(11)
