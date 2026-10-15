class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f_list = [el for el in matrix]
        for el in matrix:
            f_list.extend(el)
        return target in f_list
        