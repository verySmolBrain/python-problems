import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for p in points:
            heappush(h, (math.sqrt(p[0] ** 2 + p[1] ** 2), p))
        
        return [heappop(h)[1] for _ in range(k)]