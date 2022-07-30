x = lambda a:a+5

print(x(100)) # -> 105

print((lambda x:x*2)(10)) # -> 20

"""
In this challenge, you need to square the factorials of the first n numbers. 
Implement the function 'square_factorial' that takes 'n' as a parameter.
Write a one-line implementation of this function using an 'anonymous function'. 
To facilitate single-line implementation, you have to define another function factorial that computes the factorial of an integer.


Sample input#
5

Sample output#
[1, 1, 4, 36, 576]
"""

def factorial(n: int) -> int:

    if n == 0 or n == 1:
        return 1
    
    res = 1

    for x in range(2, n+1):
        res *= x
    
    return res

def square_factorial(n: int) -> int:

    return [(lambda a:a*a)(x) for x in map(factorial, range(n))]
