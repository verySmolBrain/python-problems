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