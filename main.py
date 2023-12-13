def categorize_age(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 18:
        return "Teenager"
    else:
        return "Adult"


def main():
    name = input("Enter your name: ")
    age_str = input("Enter your age: ")

    try:
        age = int(age_str)
        age_category = categorize_age(age)
        print(f"Hello, {name}! You are {age_category}.")
    except ValueError:
        print("Please enter a valid age as a number.")


if __name__ == "__main__":
    main()
