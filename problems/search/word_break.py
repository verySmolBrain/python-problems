class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == '':
            return True

        curword = ''
        for i in range(len(s)):
            curword += s[i]
            if curword in wordDict and self.wordBreak(s[i + 1:], wordDict):
                return True
        
        return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        canMake = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                if (word == s[i - len(word) + 1:i + 1] and canMake[i - len(word)]) or (i - len(word) == -1):
                    canMake[i] = True

        return canMake[-1]