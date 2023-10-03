data = [(3, 10), (1, 5), (2, 8), (4, 2), (2, 2)]


for i in range(len(data)):
    for j in range(1):
        if data[i][j] == data[i][j+1]:
            print(f'{data[i][j]}, {data[i][j+1]}')



sort = sorted(data, key=lambda x: x[1])
print(sort)

words = ['apple', 'banana', 'cherry', 'date', 'fig']
#words[0].
sort_str = sorted(words, key=lambda x: len(x), reverse=True)
count_char = [len(word) for word in words]
print(count_char)

word_filter = list(filter(lambda x: len(x) == 6, words))
print(word_filter)

words_dict = {'apple': 10, 'banana': 25, 'cherry': 10, 'date': 30, 'fig': 62}

list_dict = [f'{index}, {key}, {value}' for index, (key, value) in enumerate(words_dict.items()) if value == 30]
print(list_dict)
sort_dict = dict(sorted(words_dict.items(), key=lambda x: x[0]))
print(sort_dict)
