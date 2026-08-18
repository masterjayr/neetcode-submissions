class Solution:
    def rob(self, nums: List[int]) -> int:
       
       # state = i 
       # choices = i + 1, i + 2
       # combination = max(i + dfs(i+2), dfs(i+1))
       # base case => i == len(nums)
        # cache = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0

        #     if i in cache:
        #         return cache[i]

        #     cache[i] = max(nums[i] + dfs(i + 2), dfs(i+1)) # choices

        #     return cache[i]

        # return dfs(0)

        # converting using recipe
        # initialize dp array with state dimensions and base case as init value
        n = len(nums)
        # dp = [0] * (n + 1)
        # dp[n-1] = nums[n-1]
        # # start loop backwards because recurrence depends on further values i depends on i+1 nd i+2
        # for i in range(n - 2, -1, -1):
        #     dp[i] = max(nums[i] + dp[i + 2], dp[i+1])

        # return dp[0]


        # space optimize since we depend on two values alone i+1 and i+2
        # one, two = nums[n - 1], 0

        # for i in range(n-2, -1, -1):
        #     tmp = one
        #     one = max(nums[i] + two, one)
        #     two = tmp

        # return one

        # from begin to end neetcode style
        rob1, rob2 = 0, 0 

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


