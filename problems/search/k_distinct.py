class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLen, u = 0, 0, set()

        for r in range(len(s)):
            while s[r] in u:
                u.remove(s[l])
                l += 1
            
            u.add(s[r])
            maxLen = max(maxLen, (r - l) + 1)

        return maxLen