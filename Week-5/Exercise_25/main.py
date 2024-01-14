from input_helper import *

# Test the functions
num = get_integer()
print(f"Integer entered: {num}")

positive_num = get_positive_integer()
print(f"Positive integer entered: {positive_num}")

interval_num = get_integer_in_interval(1, 10)
print(f"Integer in interval entered: {interval_num}")

pair = get_integer_pair()
print(f"Integer pair entered: {pair}")
