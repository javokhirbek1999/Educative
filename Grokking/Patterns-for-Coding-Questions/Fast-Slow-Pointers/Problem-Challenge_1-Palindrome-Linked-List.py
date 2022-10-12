"""
Time: O(n)
Space: O(1)
"""

def is_palindromic_linked_list(head):

  fast, slow = head, head

  while fast and fast.next:

    fast = fast.next.next
    slow = slow.next
  
  rev = reverseLL(slow)

  copied = rev

  curr = head

  while rev.next and curr.next:
    if rev.value != curr.value:
      return False

    rev = rev.next
    curr = curr.next
  
  if rev.value != curr.value:
    return False

  revBack = reverseLL(copied)

  curr.next = revBack

  return True

def reverseLL(head):

  prev = None

  curr = head

  while curr:

    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

  return prev
