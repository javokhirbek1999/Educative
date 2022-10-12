"""

Time: O(logN)
Space: O(1)
"""

def find_happy_number(num):

  slow, fast = num, num

  while True:

    slow = move(slow)
    fast = move(move(fast))

    if slow == fast:
      break
  
  return slow == 1
  

def move(num):

  _sum = 0

  while num > 0:

    digit = num % 10

    _sum += digit * digit

    num = num//10

  return _sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
