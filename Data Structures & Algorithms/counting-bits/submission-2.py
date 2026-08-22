class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n+1):
            current = i
            while current > 0:
                if current & 1:
                    output[i] += 1
                current = current >> 1

        return output