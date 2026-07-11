class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sum(list(s.encode("utf-8") + t.encode("utf-8"))) % 2 == 0
        