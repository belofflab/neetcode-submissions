class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl_s = s.strip().lower().replace("?", "").replace(" ", "").replace("'", "")
        return cl_s == cl_s[::-1]
        