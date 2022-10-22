"""
Time: O(n)
Space: O(n)
"""

def insert(intervals, new_interval):
  
  merged = []
  
  n = len(intervals)

  i = 0

  # Skip (include in output) all the intervals that start before newInterval
  while i < n and intervals[i][1] < new_interval[0]:
    merged.append(intervals[i])
    i += 1

  # Merge all the intervals that newInterval overlaps
  while i < n and new_interval[1] >= intervals[i][0]:
    new_interval[0] = min(new_interval[0], intervals[i][0])
    new_interval[1] = max(new_interval[1], intervals[i][1])
    i += 1
  
  # Append the merged interval
  merged.append(new_interval)

  # Include the rest of the intervals that start after newInterval ends
  while i < n:
    merged.append(intervals[i])
    i += 1

  return merged


