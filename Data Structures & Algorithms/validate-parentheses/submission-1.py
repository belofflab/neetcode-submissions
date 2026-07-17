class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(0 , len(s)):
            if s[i] == s[-i - 1]:
                return False
        return True
        