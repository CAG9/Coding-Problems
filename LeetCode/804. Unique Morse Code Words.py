class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = { 'a': ".-",
                       'b' : "-...",
                       'c' : "-.-.",
                       'd' : "-..",
                       'e' : ".",
                       'f' : "..-.",
                       'g' : "--.",
                       'h' : "....",
                       'i' : "..",
                       'j' : ".---",
                       'k' : "-.-",
                       'l' : ".-..",
                       'm' :"--",
                       'n' : "-.",
                       'o' : "---",
                       'p' : ".--.",
                       'q' : "--.-",
                       'r' : ".-.",
                       's': "...",
                       't': "-",
                       'u': "..-",
                       'v' : "...-",
                       'w' : ".--",
                       'x' : "-..-",
                       'y' : "-.--",
                       'z' : "--.."}
        
        bag_of_words = []
        for word in words:
            #extract each letter form the word
            morse_letter = ''
            for letter in word:
                morse_letter += morse_code[letter]
            
            if morse_letter in bag_of_words:
                continue
            else:
                bag_of_words.append(morse_letter)
            print(bag_of_words)
        
        return len(bag_of_words)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
