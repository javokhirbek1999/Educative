"""
Time: O(n log n)
Space: O(n)
"""
from typing import List


def merge(intervals: List[int]) -> List[int]:
    
    intervals.sort(key=lambda x:x[0])

    mergedIntervals = []

    start, end = intervals[0]

    for i in range(1, len(intervals)):
        currentStart, currentEnd = intervals[i]

        if currentStart <= end:
            end = max(end, currentEnd)
        else:
            mergedIntervals.append([start, end])
            start = currentStart
            end = currentEnd

    mergedIntervals.append([start, end])

    return mergedIntervals
