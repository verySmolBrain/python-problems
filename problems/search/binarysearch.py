from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

a = search([1, 2, 3, 4, 5], 2)

print(a)