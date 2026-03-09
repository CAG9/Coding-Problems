class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        # Keep looping until n becomes 1 or we hit a cycle
        while n != 1 and n not in seen:
            seen.add(n)
            
            # Calculate the sum of squares of digits
            inner_sum = 0
            for digit in str(n):
                inner_sum += int(digit) ** 2
            
            n = inner_sum
            
        return n == 1
