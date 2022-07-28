class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stored_values  = []
        
        for number in nums:
            if number in stored_values:
                stored_values.remove(number)
            else:
                stored_values.append(number)
                
        return stored_values[0]
