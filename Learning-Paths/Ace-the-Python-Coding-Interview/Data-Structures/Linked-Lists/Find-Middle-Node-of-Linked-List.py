from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def find_mid(lst):

    slow, fast = lst.get_head(), lst.get_head()

    while fast and fast.next_element:
        if not fast.next_element.next_element:
            return slow.data
        slow = slow.next_element
        fast = fast.next_element.next_element

    return slow.data
    
