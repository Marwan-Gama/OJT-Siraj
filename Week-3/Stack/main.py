import stack

def shrink_stack(my_stack):
    temp_stack = stack.create_stack()
    count = 0

    while not stack.is_empty(my_stack):
        item = stack.pop(my_stack)
        if item == "@"  :
            max_char = 0
            while count > 0:
                temp = ord(stack.pop(temp_stack))
                if temp > max_char:
                    max_char = temp
                count -= 1
            count = 0
            stack.push(temp_stack, chr(max_char))
            stack.push(temp_stack, item)
        else:
            stack.push(temp_stack, item)
            count += 1

    return temp_stack


# Example usage
def main():
    my_stack = stack.create_stack()
    # Assuming input characters are already pushed into my_stack
    characters = ['t', 'a', 'x', '@', 'm', '@', 'g', 'r', 'b']
    for char in characters:
        stack.push(my_stack, char)

    print("Original Stack:")
    while not stack.is_empty(my_stack):
        print(stack.pop(my_stack))

    characters = ['t', 'a', 'x', '@', 'm', '@', 'g', 'r', 'b']
    for char in characters:
        stack.push(my_stack, char)

    # Shrink the stack as per requirements
    my_stack = shrink_stack(my_stack)

    print("\nShrunk Stack:")
    while not stack.is_empty(my_stack):
        print(stack.top(my_stack))
        stack.pop(my_stack)

if __name__ == "__main__":
    main()
