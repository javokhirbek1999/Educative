"""
Time: O(n log n)
Space: O(n)
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[0])
        
        removals = 0
        
        for i in range(len(intervals)-1):
            
            if intervals[i+1][0] < intervals[i][1]:
                removals += 1
                intervals[i+1][1] = min(intervals[i+1][1], intervals[i][1])
            
        
        return removals
