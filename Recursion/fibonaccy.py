def fibonaccy(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer only!"
    if n in [0, 1]:
        return n
    else:
        return fibonaccy(n-1) + fibonaccy(n-2)


print(fibonaccy(7))
