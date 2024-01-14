import sys

def usage():
    print("Usage: python script.py <argument>")
    print("Example: python script.py argument_value")
    sys.exit(1)

try:
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        raise ValueError("Incorrect number of arguments")

    # Retrieve the argument
    argument = sys.argv[1]

    print(f"{argument} squared is {argument**2}")


except ValueError as e:
    print(f"Error: {e}")
    usage()
