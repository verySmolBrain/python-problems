class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def findCombinations(nums, index, letterNumbers, path, res):
            if index == len(digits):
                return res.append(path)
            
            for c in letterNumbers[ nums[index] ]:
                findCombinations(nums, index + 1, letterNumbers, path + c, res)

        letterNumbers = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        findCombinations(digits, 0, letterNumbers, '', res)
        return res if res != [""] else []