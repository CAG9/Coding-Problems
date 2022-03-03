class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(left, right):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right +=1
            return s[left + 1 : right]
        
        result = ""
        for i in range(len(s)):
            auxresult = helper(i,i)
            if len(auxresult) > len(result):
                result = auxresult
            auxresult = helper(i,i+1) 
            if len(auxresult) > len(result):
                result = auxresult
                
        return result
