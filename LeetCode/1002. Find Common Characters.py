class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        w_len = len(words)
        result = []
        for letter in words[0]:
            count = 0
            for i,word in enumerate(words[1:]):
                #print(i+1)
                if letter in word:
                    count += 1
                    aux_word = word.replace(letter,'',1)
                    words[i+1] = aux_word
            if count == w_len -1:
                result.append(letter)
        return result
        
