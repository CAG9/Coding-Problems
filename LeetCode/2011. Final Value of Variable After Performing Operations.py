class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        Count =0
        for i in operations:
            if i == "X++" or i =="++X":
                Count +=1
            else:
                Count -= 1
        return Count
