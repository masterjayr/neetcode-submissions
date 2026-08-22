class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 # hold answer

        # loop through integer
        for i in range(32): ## 0 - 31
            bit = (n >> i) & 1 #right shift with position at i to get position at the back and AND with 1 to see if bit is 1 or 0
            res = res | (bit << (31 - i)) #left shift to position on right and OR with 0
        return res