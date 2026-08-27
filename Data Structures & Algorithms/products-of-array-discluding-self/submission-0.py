class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            temp_c = 1
            for el in temp:
                temp_c *= el
            result.append(temp_c)
        return result
        