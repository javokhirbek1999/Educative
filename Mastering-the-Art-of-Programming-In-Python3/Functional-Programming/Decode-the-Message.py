"""
Challenge #1:

In this problem, you’re required to decode a message. You have to implement a function clean_message decorated by decode. By decoding, we mean:

Filter out all the characters that are not the digits.
    - Sort the digits in the ascending order.
    - Map the digits to their actual values.

Mapping is a simple procedure. If you read digit 0, it means that its actual value is 9. Similarly, if you read digit 1, its actual value would be 8. The following figure explains the mapping procedure:

Mapping example:
 
0   1   2   3   4   5   6   7   8   9
|   |   |   |   |   |   |   |   |   |
9   8   7   6   5   4   3   2   1   0

"""

import functools


def decode(function):
    @functools.wraps(function)
    def wrapper(message: str) -> str:

        result = function(message)

        result = result.lower()

        result = "".join(sorted(result))

        digits = {'0': 9, '1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1, '9': 0}
        
        res = ""

        for char in result:
            res += str(digits[char])

        return res
    
    return wrapper
    

@decode
def clean_message(message: str) -> str:
    
    digits = {'0': 9, '1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1, '9': 0}

    cleaned = ""

    for char in message:
        if char in digits:
            cleaned += char
    
    return cleaned
