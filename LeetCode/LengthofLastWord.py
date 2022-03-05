class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        SplitedString = s.split(' ')
        print(SplitedString)
        count  = -1
        while True:
            if SplitedString[count] != '':
                return len(SplitedString[count])
            count -=1
