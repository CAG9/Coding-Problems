class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        str_dict = dict()
        
        for index,string in enumerate(strs):
            
            
            new_string = ''.join(sorted(string))
            
            if new_string in str_dict:
                str_dict[new_string] += [string] 
            else:
                str_dict[new_string] = [string]
                
        return [i for i in str_dict.values()]
