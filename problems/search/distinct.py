from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = Counter(nums)

        return any(i > 1 for i in distinct.values())