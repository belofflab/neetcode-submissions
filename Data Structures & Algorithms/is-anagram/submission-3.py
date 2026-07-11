class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s.encode("utf-8"))) == sorted(list(t.encode("utf-8")))