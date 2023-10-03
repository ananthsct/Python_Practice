str = "ababcade"

# for i in str:
#     if str.count(i) > 1:
#         str = str.lstrip(i)
# print(str)

count = 0
for i in str:
    if i in str:
        count += 1
    if count > 1:
        str = str.lstrip(i)
print(str)
