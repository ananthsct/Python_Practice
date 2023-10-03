def approved_requests(approved, requests):
    day_approval_count = {}  # Dictionary to store the approval count for each day

    # Count the approvals for each day
    for approval_list in approved:
        for day in approval_list:
            day_approval_count[day] = day_approval_count.get(day, 0) + 1

    result = []

    # Check each requested day
    for day in requests:
        if day_approval_count.get(day, 0) < 2:  # Check the limit of two approvals
            result.append(day)
            #day_approval_count[day] = day_approval_count.get(day, 0) + 1

    return result

approved_1 = [
  [3, 6, 11, 15, 20, 23, 25, 28, 29],
  [7, 21, 23, 27, 30]
]
requests_1_1 = [9, 13, 17, 23, 25]
# Test cases
print(approved_requests(approved_1, requests_1_1))
# print(approved_requests(approved_2, requests_2_1))
# print(approved_requests(approved_2, requests_2_2))
# print(approved_requests(approved_2, requests_2_3))
# print(approved_requests(approved_3, requests_3_1))
# print(approved_requests(approved_4, requests_4_1))
