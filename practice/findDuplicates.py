nums = [9, 13, 13, 17, 18, 23, 25]
unique = []
unique2 = []
unique3 = [i for i in nums if i not in unique2]
# unique2 = [i for i in nums if i % 2 == 0]

print(unique3)

for i in nums:
    if i not in unique:
        unique.append(i)

print(unique)
