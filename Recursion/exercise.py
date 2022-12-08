# def recursion(n):
#     if n < 1:
#         print("n is less than 1")
#     else:
#         recursion(n-1)
#         print(n)


# recursion(5)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))
