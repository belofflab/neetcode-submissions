class Solution:
    def isPalindrome(self, s: str) -> bool:
        ex_chrs = {",",".", "?", "!"}
        cl_s = s.strip().lower().replace("?", "")

        return cl_s == cl_s[::-1]
        