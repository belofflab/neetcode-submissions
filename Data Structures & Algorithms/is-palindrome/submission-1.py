class Solution:
    def isPalindrome(self, s: str) -> bool:
        return len(set(list(s.strip().lower().split().encode("utf-8")))) % 2 == 0
        