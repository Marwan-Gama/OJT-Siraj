# Q1
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_max(lst[1:]))

# Q2
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], find_min(lst[1:]))

# Q3
def sum_even(lst):
    if not lst:
        return 0
    elif lst[0] % 2 == 0:
        return lst[0] + sum_even(lst[1:])
    else:
        return sum_even(lst[1:])

# Q4
def product(lst):
    if not lst:
        return 1
    else:
        return lst[0] * product(lst[1:])

# Q5
def average(lst):
    if not lst:
        return 0
    else:
        return sum(lst) / len(lst)


# Example list
arr = [3, 7, 12, 5, 8, 10]

# Output results
print("Maximum:", find_max(arr))
print("Minimum:", find_min(arr))
print("Sum of even items:", sum_even(arr))
print("Product of all items:", product(arr))
print("Average of items:", average(arr))
