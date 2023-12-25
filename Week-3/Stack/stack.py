def create_stack():
    return []

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()

def top(stack):
    if not is_empty(stack):
        return stack[-1]

def is_empty(stack):
    return len(stack) == 0
