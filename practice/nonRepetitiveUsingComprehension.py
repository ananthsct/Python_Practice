def first_non_repeating_char(string, n):
    # Create a dictionary to store the count of characters
    char_count = {char.lower(): string.count(char) for char in string}

    # Create a list of characters that appear only once
    non_repeating_chars = [char for char, count in char_count.items() if count == 1]

    # Filter out non-repeating characters that are not in the original order
    char_order = [char for char in string if char.lower() in non_repeating_chars]

    # If there are non-repeating characters, return the one at index 'n'
    if n < len(char_order):
        return char_order[n]

    # If there are no non-repeating characters, return None
    return None

# Example usage:
input_string = "aAbBcCDeeG"
result = first_non_repeating_char(input_string, 1)

if result is not None:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found in the string.")
