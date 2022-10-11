"""
Time: O(n)
Space: O(1)
"""

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  
  slow, fast = head, head
  
  while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

    if fast == slow:
      cycle_length = findLen(slow)
      break
  
  return startOfList(head, cycle_length)

def startOfList(head, cycle_length):

  pointer1 = head
  pointer2 = head

  for _ in range(cycle_length):
    pointer2 = pointer2.next
  
  while pointer1 != pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  
  return pointer1



def findLen(slow):

  length = 0

  curr = slow

  while True:

    curr = curr.next

    length += 1

    if curr is slow:
      break

  return length


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
