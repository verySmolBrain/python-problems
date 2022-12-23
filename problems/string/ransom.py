class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineLetters = {}
        for c in magazine:
            magazineLetters[c] = magazineLetters.get(c, 0) + 1
        
        for c in ransomNote:
            magazineLetters[c] = magazineLetters.get(c, 0) - 1
            if magazineLetters[c] < 0:
                return False
        
        return True