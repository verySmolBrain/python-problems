class Solution: # Iteratively
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sb = [[]]
        for num in nums:
            sb += [[num] + item for item in sb]
        
        return sb

class Solution: # DFS
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def findSubsets(nums, path, sb):
            sb.append(path)
            for i in range(len(nums)):
                findSubsets(nums[i + 1:], path + [nums[i]], sb)

        sb = []
        findSubsets(nums, [], sb)
        return sb