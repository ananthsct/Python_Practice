def are_values_equal(row, start_col, end_col):
    for i in range(start_col, end_col + 1):
        if row[i] != row[start_col]:
            return False
    return True

def find_rows_with_same_values(data, start_col, end_col):
    result = []
    for row_num, row in enumerate(data):
        if are_values_equal(row, start_col, end_col):
            result.append(row_num)
    return result

# Example data (replace this with your actual data)
data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
    [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
]

# Specify the columns F to AI (0-based index)
start_column = 5  # Column F
end_column = 10   # Column AI

# Find row numbers with the same values in the specified columns
result_row_numbers = find_rows_with_same_values(data, start_column, end_column)

# Print the result
if len(result_row_numbers) > 0:
    print("Row numbers with the same values from column F to AI:")
    print(result_row_numbers)
else:
    print("No rows with the same values from column F to AI.")
