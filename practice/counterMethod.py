from collections import Counter

s = 'AaabrnskrBrbaa'

# Count the occurrences of each character in the string
count = Counter(s)
print(count)

# Sort the items by occurrence in descending order and then by position in the string in ascending order
sorted_items = sorted(count.items(), key=lambda x: (-x[1], s.index(x[0])))
print(type(sorted_items))
print(sorted_items)

# Get the item with the second largest occurrence
second_largest_item = sorted_items[1]

print(second_largest_item[0])  # Output: 'a'
