from collections import deque

class Solution:
    def myAtoi(self, s: str) -> int:
        s, digits = s.strip(), deque()
        sign = False if len(s) > 1 and s[0] == '-' else True
        if len(s) > 1 and (s[0] == '+' or s[0] == '-'):
            s = s[1:]

        for c in s:
            if not c.isdigit():
                break
            digits.append(int(c))
        
        ans, n = 0, len(digits)
        for i in range(n - 1, -1, -1):
            a = 1
            for j in range(0, i):
                a *= 10
            ans += digits.popleft() * a

        ans = ans if sign else ans * -1
        ans = min(ans, 2 ** 31 - 1)
        ans = max(-(2 ** 31), ans)
        
        return ans