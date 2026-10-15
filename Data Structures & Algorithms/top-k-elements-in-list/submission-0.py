class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = [] 
        for num in set(nums):
            elcnt = 0
            for j in range(len(nums)):
                if nums[j] == num:
                    elcnt += 1
            if elcnt >= k:
                elements.append(num)
        return elements
            