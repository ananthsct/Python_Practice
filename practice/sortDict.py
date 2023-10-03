original_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

# Sort the dictionary by keys
sorted_dict_by_key = dict(sorted(original_dict.items()))
print(sorted_dict_by_key)
# Output: {'apple': 3, 'banana': 1, 'cherry': 2}

# Sort the dictionary by values
sorted_dict_by_value = dict(sorted(original_dict.items(), key=lambda item: item[1]))
print(sorted_dict_by_value)
# Output: {'banana': 1, 'cherry': 2, 'apple': 3}

numbers = [1, 2, 3, 3, 3]
num_2 = (1, 2, 3, 3, 3)
dict_num = dict.fromkeys(numbers, 0)
dict_num2 = dict.fromkeys(num_2, 0)
print(dict_num)
print(dict_num2)
