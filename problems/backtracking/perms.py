class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(nums, perms, path):
            if not nums:
                perms.append(path)
            
            for i in range(len(nums)):
                permutations(nums[:i] + nums[i + 1:], perms, path + [nums[i]])
        
        perms = []
        permutations(nums, perms, [])
        return perms
