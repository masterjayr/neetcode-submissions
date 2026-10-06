class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # count = 0
        # # naive approach
        # for L in range(len(arr)):
        #     currSum = arr[L]
        #     for R in range(L+1, len(arr)):
        #         if R-L+1 > k:
        #             break
        #         currSum += arr[R]
        #         if R-L+1 == k:
        #             avg = currSum // k

        #             if avg >= threshold:
        #                 count += 1

        # return count

        # sliding window
        L = 0
        currSum = 0
        total = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                currSum -= arr[L]
                L += 1
            
            currSum += arr[R]
            if R - L + 1 == k:
                avg = currSum // k

                if avg >= threshold:
                    total += 1
        return total

