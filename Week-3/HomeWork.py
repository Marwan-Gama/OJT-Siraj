# 1 - Function to sum the digits of a number recursively
def sum_digit(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digit(num // 10)


# 2 - Function to count the number of digits in a number recursively
def get_num_digits(num):
    if num == 0:
        return 0
    return 1 + get_num_digits(num // 10)


# 3 - Function to count the number of odd digits in a number recursively
def CountOddDigits(num):
    if num == 0:
        return 0
    return (num % 10) % 2 + CountOddDigits(num // 10)


# 4 - Function to print a string in reverse recursively
def print_reverse_str(string):
    if len(string) == 0:
        return
    print(string[-1], end='')
    print_reverse_str(string[:-1])


# 5 - Function to print a string in reverse recursively with type checking
def recurgun(s):
    if isinstance(s, str):
        if len(s) == 0:
            return
        else:
            print(s[-1], end='')
            recurgun(s[:-1])
    else:
        print("Input must be a string")


# 6 - Function to multiply two numbers without using the '*' sign recursively
def multiply(x, y):
    if y:
        return x + multiply(x, y - 1)
    else:
        return 0


# 7 - Function to perform division recursively
def Division(num1, num2):
    if num1 == 0 or num1 < num2:
        return 0
    elif num1 - num2 < num2 and num1 != 0:
        return 1
    elif num2 == 0:
        return 'error'
    return Division(num1 - num2, num2) + 1


# 8 - Function to check if a string is a palindrome recursively
def check_palindrome(word):
    if len(word) == 0:
        return True
    return isPal(word, 0, len(word) - 1)


def isPal(string, start, end):
    # If there is only one character
    if start == end:
        return True

    # If first and last characters do not match
    if string[start] != string[end]:
        return False

    # Check if middle substring is also a palindrome or not
    if start < end + 1:
        return isPal(string, start + 1, end - 1)
