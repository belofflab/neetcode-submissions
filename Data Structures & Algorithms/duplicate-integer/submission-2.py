class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[right] == nums[right-1]:
                return True
            left += 1
        return False
        