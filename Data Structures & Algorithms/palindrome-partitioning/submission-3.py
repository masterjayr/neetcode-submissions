class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, curPartition):
            if i == len(s):
                res.append(curPartition.copy())
                return 

            for j in range(i+1, len(s)+1):
                if self.isPali(s[i:j]):
                    curPartition.append(s[i:j])
                    backtrack(j, curPartition)
                    curPartition.pop()

            

        backtrack(0, [])
        return res

    def isPali(self, sub): 
        return sub == sub[::-1]
            