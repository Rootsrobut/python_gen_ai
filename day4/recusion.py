def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) 



def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 7
for i in range(n):
    print(fibonacci(i), end=" ") 


def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)
print(sum_natural(5))  


def sum_even(n):
    if n == 0:
        return 0
    return 2 * n + sum_even(n - 1)

print(sum_even(5)) 

def sum_odd(n):
    if n == 0:
        return 0
    return (2 * n - 1) + sum_odd(n - 1)

print(sum_odd(5))  


def print_odds(n):
    if n == 0:
        return
    print_odds(n - 1)
    if n % 2 != 0:
        print(n, end=" ")
print_odds(10)

print()  

def print_evens(n):
    if n == 0:
        return
    print_evens(n - 1)
    if n % 2 == 0:
        print(n, end=" ")
print_evens(10) 




