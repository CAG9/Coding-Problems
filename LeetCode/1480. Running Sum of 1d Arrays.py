class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_result = []
        for i in range(len(nums)):
            sum_result.append(sum(nums[:i+1]))
        
        return sum_result
