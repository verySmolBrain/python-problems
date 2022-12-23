from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        slen = len(s)
        c = Counter(s)
        odd_count = sum(1 for e in c if c[e] % 2 != 0)

        return (slen - odd_count) + 1 if odd_count > 0 else slen