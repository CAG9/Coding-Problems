class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_check = n/2
        
        myhash = {}

        for i in nums:
            if i in myhash:
                myhash[i] +=1
            else:
                myhash[i] = 1
        
        for element in myhash:
            if myhash[element] >= majority_check:
                return element
