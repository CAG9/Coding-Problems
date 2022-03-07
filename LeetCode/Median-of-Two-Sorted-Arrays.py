class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedarray = nums1 + nums2
        mergedarray = sorted(mergedarray)
        print(mergedarray)
        if len(mergedarray) % 2 == 0:
            part1 = mergedarray[(len(mergedarray)//2)]
            part2 = mergedarray[(len(mergedarray)//2)-1]
            
            return (part1+part2) / 2
        
        else:
            return mergedarray[floor(len(mergedarray)/2)]
