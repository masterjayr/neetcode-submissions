# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helper(pairs, 0, len(pairs)-1)

    
    def helper(self, pairs, s, e):

        if e - s + 1 <= 1:
            return pairs 

        mid = s + (e - s) // 2
        self.helper(pairs, s, mid)
        self.helper(pairs, mid+1, e)

        self.merge(pairs, s, mid, e)

        return pairs

    def merge(self, pairs, start, mid, end):
        L = pairs[start:mid+1]
        R = pairs[mid+1:end+1]

        i = j = 0
        k = start

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j+=1 
            k += 1

        while i < len(L):
            pairs[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1


