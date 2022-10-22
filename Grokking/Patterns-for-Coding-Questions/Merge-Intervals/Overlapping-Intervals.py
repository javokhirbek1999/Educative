"""
Time: O(n log n)
Space: O(n) <-- Timesort uses extra space
"""
from typing import List


def overlap(intervals: List[int]) -> bool:

    intervals.sort(key=lambda x:x[0])

    start, end = intervals[0]

    for i in range(1, len(intervals)):
        currentStart, currentEnd = intervals[i]

        if currentStart <= end:
            return True
        else:
            start = currentStart
            end = currentEnd
    
    return False
  
