class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        finallist = []
        for index in range(0,len(words)):
            if x in words[index]:
                finallist.append(index)
            else:
                None
        return finallist
