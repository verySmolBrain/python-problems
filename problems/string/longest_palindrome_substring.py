class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        pos, longest = defaultdict(deque), ''

        for i, c in enumerate(s):
            pos[c].append(i)
        
        for c in s:
            cur = pos[c].popleft()
            for p in pos[c]:
                checkStr = s[cur:p + 1]
                if isPalindrome(checkStr):
                    longest = checkStr if len(checkStr) > len(longest) else longest
        
        return longest if (longest != '' and len(s) > 0) else s[0]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def fromMiddle(s, l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1:r]

        res = ''

        for i in range(len(s)):
            res = max(fromMiddle(s, i, i), fromMiddle(s, i, i + 1), res, key = len)
        
        return res
    # Gigabrain solution