from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boeyr Moore's Algorithm
        count = 1
        res = nums[0]

        for num in nums[1:]:
            if num != res:
                count -= 1
                if count == 0:
                    res = num
                    count = 1
            else:
                count += 1
        
        return res

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        return Counter(nums).most_common(1)[0][0]
    # Create counter from nums
    # Get only 1 most common element
    # In this form [(element, count)]
    # So [0][0]