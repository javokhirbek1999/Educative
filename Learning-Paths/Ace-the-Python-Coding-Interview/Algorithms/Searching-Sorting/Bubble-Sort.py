"""
Time: O(n^2)
Space: O(1)
"""

def bubbleSort(arr: list) -> None:
    
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
