class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(curSum, 0) + num
            # If curSum is negative, we can discard it since it will
            # bring nothing to future sums
            maxSum = max(curSum, maxSum)
        
        return maxSum