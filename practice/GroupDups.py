from itertools import groupby


def group_consecutive(input_frequencies):

    dict1 = {i: input_frequencies.count(i) for i in input_frequencies}
    #sort_dict = dict(sorted(dict1.items()))
    output = []
    for key, value in dict1.items():
        tuple_element = (key,) * value
        print(type(tuple_element))
        output.append(tuple_element)

    return sorted(output)


input_frequencies = [2, 3, 4, 2, 2, 1, 1, 1, 3]
output = group_consecutive(input_frequencies)
print(output)
