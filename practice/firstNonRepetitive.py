def first_non_repeating_char(string, n):
    # Create a dictionary to store the count of characters
    char_count = {}

    # Create a list to maintain the order of appearance of characters
    char_order = []

    # Populate the char_count dictionary and char_order list
    for char in string:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
            # char_count[char_lower] = char_count.get(char_lower, 0) + 1

        else:
            char_count[char_lower] = 1
            char_order.append(char)
    print(char_count)
    print(char_order)
    new = []
    # Find the first non-repeating character
    for char in char_order:
        if char_count[char.lower()] == 1:
            # Check if the original character was uppercase and print it in uppercase
            new.append(char)
    return new[n]

    # If there are no non-repeating characters, return None
    return None


# Example usage:
input_string = "aAbBcCDeeG"
result = first_non_repeating_char(input_string, 1)

if result is not None:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found in the string.")

#count = {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 2, 'g': 1}
#sorted_items = sorted(count.items(), key=lambda x: (-x[1], input_string.index(x[0])))
