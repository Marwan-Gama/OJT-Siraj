def get_integer(prompt="Enter an integer: "):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_positive_integer(prompt="Enter a positive integer: "):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def get_integer_in_interval(a, b):
    prompt = f"Enter an integer in the interval [{a}, {b}]: "
    while True:
        try:
            value = int(input(prompt))
            if a <= value <= b:
                return value
            else:
                print(f"Please enter an integer in the interval [{a}, {b}].")
        except ValueError:
            print("Please enter a valid integer.")

def get_integer_pair(prompt="Enter a pair of two integers (x y): "):
    while True:
        try:
            values = input(prompt).split()
            if len(values) == 2:
                x, y = map(int, values)
                return x, y
            else:
                print("Please enter two integers separated by a space.")
        except ValueError:
            print("Please enter valid integers.")
