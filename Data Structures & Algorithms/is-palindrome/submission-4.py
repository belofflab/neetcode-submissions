class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl_s = s.strip().lower()
        return s == s[::-1]
        