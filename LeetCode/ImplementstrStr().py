class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        
        NeedleLenght = len(needle)
        for step in range(len(haystack) + 1 - len(needle)):
            if haystack[step:step+NeedleLenght] == needle:
                return step
            
        return -1
