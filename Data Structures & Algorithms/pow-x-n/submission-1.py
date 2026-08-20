class Solution:
    def myPow(self, x: float, n: int) -> float:
        # so idea is x^2 => x^1 x x^1 so if n is odd say x^3 it's x * x^1 * x^1 
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res 

        res = helper(x, abs(n))

        return res if n >= 0 else 1 / res 