class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cl = s.lower().strip().replace("?", "").replace(" ", "")
        return s_cl == s_cl[::-1]
        