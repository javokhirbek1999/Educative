from MinHeap import MinHeap


def findKSmallest(lst, k):
    
    if len(lst) < k:
        return []

    heap = MinHeap()

    for i in lst:
        heap.insert(i)
    

    res = []

    for _ in range(k):
        res.append(heap.removeMin())
    
    return res
