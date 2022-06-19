def convertMax(maxHeap):

    n = len(maxHeap)
    
    for i in range(len(maxHeap)-1, -1, -1):
        heapify(maxHeap, n, i)

    return maxHeap

def heapify(maxHeap, n, index):

    l = 2 * index + 1
    r = 2 * index + 2

    if l < n and maxHeap[l] < maxHeap[index]:
        smallest = l
    else:
        smallest = index
    
    if r < n and maxHeap[r] < maxHeap[smallest]:
        smallest = r
    if smallest != index:
        maxHeap[smallest], maxHeap[index] = maxHeap[index], maxHeap[smallest]
        heapify(maxHeap, n, smallest)
