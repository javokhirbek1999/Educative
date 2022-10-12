"""
Time: O(n)
Space: O(1)

"""

def find_middle_of_linked_list(head):

  fast, slow = head, head


  while fast and fast.next:

    slow = slow.next
    fast = fast.next.next
  
  return slow
