# Define a list of words
words = ["apple", "baneana", "chearry", "date"]

# Convert each word into a set of characters
word_sets = [set(word) for word in words]
print(word_sets)

# Find the common characters by taking the intersection of all sets
common_characters = set.intersection(*word_sets)
print(common_characters)

# Convert the result set back to a sorted list for readability
common_characters_list = ', '.join(sorted(list(common_characters)))
print(type(common_characters_list))
# Print the common characters
print("Common characters:", common_characters_list)

