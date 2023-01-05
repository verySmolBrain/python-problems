class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: return False

        target = s // 2
        dp = [True] + [False] * target

        for x in nums:
            dp = [dp[s] or (s >= x and dp[s - x]) for s in range(target + 1)]
            if dp[target]: return True
        return False