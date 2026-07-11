class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ix,i in enumerate(nums):
            for jx,j in enumerate(nums):
                if i + j == target:
                    return [ix,jx]