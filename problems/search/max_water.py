from collections import defaultdict

class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = defaultdict(lambda: -1)

        for (i, n1) in enumerate(height):
            for (j, n2) in enumerate(height):
                if n2 >= n1: most[i] = max(most[i], abs(j - i) * n1)
        
        return max(most.values())

from collections import defaultdict

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        most = 0

        while l <= r:
            cur_height = (r - l) * height[l] if height[l] < height[r] else (r - l) * height[r]
            most = max(most, cur_height)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return most