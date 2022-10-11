"""
Time: O(n)
Space: O(1)
"""


def has_cycle(head):
  
  if not head or not head.next:
    return False

  first, slow = head, head

  while first and first.next:

    slow = slow.next
    first = first.next.next

    if first is slow:
      return True
  
  return False
