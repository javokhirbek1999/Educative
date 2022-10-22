"""
Time: O(n log n)
Space: O(n)
"""
from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]):

    merged = []

    intervals.append(new_interval)

    intervals.sort(key=lambda x:x[0])

    start, end = intervals[0]
    
    for i in range(1, len(intervals)):

        currentStart, currentEnd = intervals[i]

        if currentStart < end:
            end = max(end, currentEnd)
        else:
            merged.append([start, end])
            start = currentStart
            end = currentEnd
    
    merged.append([start, end])

    return merged

