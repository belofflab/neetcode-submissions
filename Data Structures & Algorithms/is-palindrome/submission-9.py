class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cl = "".join(i for i in s.lower() if i.is_alpha())
        return s_cl == s_cl[::-1]
        