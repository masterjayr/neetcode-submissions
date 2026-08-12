class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(0, n+1):
            currentNo = i
            while currentNo > 0:
                if currentNo & 1:
                    output[i]+= 1
                currentNo = currentNo >> 1

        return output