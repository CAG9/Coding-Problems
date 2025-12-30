class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible = 0
        nondivisible = 0
        for number in range(1,n+1):
            if number % m == 0:
                divisible += number 
            else:
                nondivisible += number
        return nondivisible - divisible
