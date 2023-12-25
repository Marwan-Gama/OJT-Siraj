'''
• The power set of a set S, P(S), is the set of all subsets of S, including the empty set
• and S itself
• For example, P({1,3,6}) = {{}, {1}, {3}, {6}, {1,3}, {1,6}, {3,6}, {1,3,6}}
• Write a generator function that returns the power set of a given set
'''

def powerset(s):
    s = list(s)
    n = len(s)
    if n == 0:
        return [[]]
    element = s.pop()
    subsets = powerset(s)
    new_subsets = [subset + [element] for subset in subsets]
    return subsets + new_subsets

# Example usage:
input_set = {1, 3, 6}
result = powerset(input_set)

print("Power set of", input_set, "is:", result)
