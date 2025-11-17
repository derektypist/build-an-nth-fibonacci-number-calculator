def fibonacci(n):
    sequence = [0,1]
    if n<=1:
        return sequence[n]
    i = 1
    while i<n:
        sequence.append(sequence[i] + sequence[i-1])
        i += 1
    return sequence[n]


# Examples
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))
