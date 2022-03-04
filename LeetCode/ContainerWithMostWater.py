class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        leftpointer = 0
        rightpointer = len(height) - 1
        
        while( leftpointer < rightpointer):
            area = (rightpointer - leftpointer) * min(height[leftpointer], height[rightpointer])
            result = max(result,area)
            
            if height[leftpointer] < height[rightpointer]:
                leftpointer += 1
            else:
                rightpointer -= 1
            
        return result
        
