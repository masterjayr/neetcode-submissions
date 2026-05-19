# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helper(pairs, 0, len(pairs)-1)

    
    def helper(self, pairs, s, e):
        
        if e - s + 1 <= 1:
            return pairs 

        left = s 
        pivot = pairs[e]

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[i], pairs[left] = pairs[left], pairs[i]
                left+=1
        
        pairs[e] = pairs[left]
        pairs[left] = pivot 

        self.helper(pairs, s, left-1)
        self.helper(pairs, left+1, e)

        return pairs
        