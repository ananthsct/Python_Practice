# Pattern 1
# Outer loop defines the number of rows
# Inner loop controls the number of spaces and *
n = 5
for i in range(1, n+1):
    #print('')
    for j in range(0):
        print(' ', end='')
    for k in range(i):
        print('* ', end='')
    print()
for i in range(1, n):
    for j in range(n-i, 0, -1):
        print('* ', end='')
    for k in range(1, n-1):
        print('', end='')
    print()

print()
# Pattern 2
# Define the number of rows for the pattern
num_rows = 6

# Outer loop for each row
for i in range(1, num_rows + 1):
    # Print spaces for alignment
    for j in range(num_rows - i):
        print(" ", end="")

    # Print asterisks for the current row
    for k in range(i):
        print("* ", end="")

    # Move to the next line for the next row
    print()
for i in range(1, num_rows):
    # Print spaces for alignment
    for j in range(i):
        print(" ", end="")
    # Print asterisks for the current row
    for k in range(num_rows-i):
        print("* ", end="")
    print()
