class Solution:
    def isValid(self, s: str) -> bool:
        counter = {}
        for el in s:
            counter[el] = counter.get("el", 0) + 1
        
        return sum(counter.values()) % 2 == 0
        