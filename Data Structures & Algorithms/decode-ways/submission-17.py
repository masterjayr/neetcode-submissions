class Solution:
    def numDecodings(self, s: str) -> int:
        # following my dp recipe 

        # state => i
        # choices=> take character i, take characters i:i+1(inclusive)
        # validity -> if i is not 0 and i:i+1(inclusive) < 26
        # base case -> i == len(s) == 1 way
        # combine -> dfs(i+1) + dfs(i + 2) i depending on just i + 1, i + 2 -> can shrink into two variables

        cache = {len(s): 1}
        def dfs(i):
            if i in cache:
                return cache[i]

            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            cache[i] = res
            return cache[i]


        # return dfs(0)

        # conversion to true dp
        n = len(s)
        dp = [0] * (n+2)
        dp[n] =  1

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            else:
                dp[i] = dp[i+1]

            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]

        return dp[0]




        

        

