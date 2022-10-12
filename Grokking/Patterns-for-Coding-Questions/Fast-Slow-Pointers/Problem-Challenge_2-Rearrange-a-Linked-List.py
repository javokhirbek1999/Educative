"""
Time: O(n)
Space: O(1)
"""

def reorder(head):
  
  slow, fast = head, head

  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

  rev = reverse(slow)

  curr = head

  while curr and rev:
    _next = curr.next
    _next2 = rev.next
    rev.next = _next
    curr.next = rev
    curr = _next
    rev = _next2
  
  curr.next = None
  return head
  

def reverse(head):

  curr = head
  prev = None

  while curr:
    _next = curr.next
    curr.next = prev
    prev = curr
    curr = _next
  
  return prev
