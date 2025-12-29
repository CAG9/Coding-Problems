class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arraysum = sum(nums)
        if arraysum % k == 0:
            return 0
        else:
            return arraysum % k
