class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for n in nums:
            if n == 0: red += 1
            if n == 1: white += 1
            if n == 2: blue += 1
        
        nums[:red] = [0] * red
        nums[red:red + white] = [1] * white
        nums[red + white:] = [2] * blue