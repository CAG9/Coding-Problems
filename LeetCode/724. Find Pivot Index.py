class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        left_sum = 0
        for pivot in range(len(nums)):
            right_sum = total_sum - left_sum - nums[pivot]
            if left_sum == right_sum:
                return pivot
            left_sum += nums[pivot]
            
        return -1
            
