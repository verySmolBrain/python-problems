# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        last_good = 0

        while left <= right:
            mid = left + (right - left) // 2
            print(mid, left, right)
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left