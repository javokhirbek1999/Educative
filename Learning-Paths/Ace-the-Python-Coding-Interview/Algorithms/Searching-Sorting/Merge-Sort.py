"""
Paradigm: Divide and Conquer

Time: O(n log n)
Space: O(n)
"""
def merge_sort(arr: list) -> None:


    mid = len(arr)//2

    if mid <= 0:
        return arr

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)


    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
