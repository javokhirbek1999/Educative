from MaxHeap import MaxHeap


def findKLargest(lst, k):
    
    heap = MaxHeap()

    for i in lst:
        heap.insert(i)

    return [heap.removeMax() for _ in range(k)]
