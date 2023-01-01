class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START, END , i = 0
        intervals = sorted(intervals, key = lambda x: x[START]
        
        while i < len(intervals) - 1:
            if intervals[i][END] >= intervals[i + 1][START]:
                intervals[i][END] = max(intervals[i][END], intervals[i + 1][END])
                del intervals[i + 1]
            else:
                i += 1
        
        return intervals
