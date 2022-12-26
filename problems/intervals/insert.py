class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START, END = 0, 1

        intervals.append(newInterval)

        out = []
        for interval in sorted(intervals, key = lambda x: x[START]):
            if out != [] and interval[START] <= out[-1][END]:
                out[-1][END] = max(interval[END], out[-1][END])
            else:
                out.append(interval)
        
        return out
    

# class Solution: Gigachad solution
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         START, END = 0, 1
#         s, e = newInterval[START], newInterval[END]
#         l, r = [], []

#         for i in intervals:
#             if i[START] > e:
#                 r.append(i)
#             elif i[END] < s:
#                 l.append(i)
#             else:
#                 s = min(s, i[START])
#                 e = max(e, i[END])
        
#         return l + [[s, e]] + r