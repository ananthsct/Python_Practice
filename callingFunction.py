from package.math_operations import Math

result1 = Math.add_new(5, 3)
# result = add_new(5, 3)
print(result1)  # Output: 8

L1 = [1, 8, 5, 6]
L2 = [2, 5, 6]
L1.extend(L2)
print(L1)
L3 = sorted(L1)
max = max(L3)
print(max)
print(L3)
L3.reverse()
print(L3)

fruits = ["apple", "banana", "cherry", "date", "elderberry", 2, 6, 89, 50]
l1 = []
l2 = []
new_fr = [fruit for fruit in fruits if type(fruit) == str]
l2 = [item for item in fruits if item not in new_fr]
print(new_fr)
print(l2)
# l1 = list(filter(lambda x: isinstance(x, str), fruits))
new_fr = list(filter(lambda x: isinstance(x, str), fruits))
print(new_fr)
# Lambda function with if-else statement
conditional_lambda = lambda x: "Even" if x % 2 == 0 else "Odd"

# Test the lambda function
print(conditional_lambda(4))  # Output: Even
print(conditional_lambda(7))  # Output: Odd
