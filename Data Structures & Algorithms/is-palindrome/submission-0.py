class Solution:
    def isPalindrome(self, s: str) -> bool:
        return len(set(list(s.encode("utf-8")))) % 2 == 0
        