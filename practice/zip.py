from itertools import groupby

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
combined = list(zip(list2, list1))
print(combined)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


list3, list4 = zip(*combined)
print(list(list3))
print(list4)


input_frequencies = [2, 3, 4, 2, 2, 1, 1, 1, 3]
unique = set(input_frequencies)
new_list = []

for key, group in groupby(input_frequencies):
    new_list.append(list(group))
print(new_list)
