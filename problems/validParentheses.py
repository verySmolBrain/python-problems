class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in brackets.values():
                stack.append(c)
            elif c in brackets.keys():
                if stack == [] or stack.pop() != brackets[c]:
                    return False
        
        if stack == []:
            return True
        else:
            return False