class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative = 0 
        for array in grid:
            for num in array:
                if num < 0:
                    negative += 1
        return negative 
