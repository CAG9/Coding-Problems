class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        Count = 0
        for i,val in enumerate(nums):
            if i % 2 == 0:
                Count += val
            else:
                Count -= val
        return Count
        
