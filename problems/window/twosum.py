class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(enumerate(nums), key = lambda i: i[1])
        low = 0
        high = len(nums) - 1
        
        while low < high:
            twosum = sortedNums[low][1] + sortedNums[high][1]
            
            if twosum == target:
                return [sortedNums[low][0], sortedNums[high][0]]
            elif twosum < target:
                low += 1
            else:
                high -= 1