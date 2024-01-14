def tilingRectangle(n, m):
    squares = []
    if n == m:
        squares.append((m, m))
        return squares

    while n > 0 and m > 0:
        if n > m:
            n -= m
            squares.append((m, m))
        else:
            m -= n
            squares.append((n, n))

    return squares

# Example usage
n = 8
m = 5
result = tilingRectangle(n, m)
print(f"The minimum number of integer-sided squares to tile a {n} x {m} rectangle is: {result}")
