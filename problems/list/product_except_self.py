class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        tmp = 1
        for j in range(len(nums) - 2, -1, -1):
            tmp *= nums[j + 1]
            res[j] *= tmp
        
        return res