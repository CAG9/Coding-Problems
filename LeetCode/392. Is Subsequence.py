class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        pointer_s = 0 
        pointer_t = 0
        
        while(pointer_t < len(t)):
            if t[pointer_t] == s[pointer_s]:
                pointer_s += 1
                
            if pointer_s == len(s):
                return True
            
            pointer_t += 1 
        return False
