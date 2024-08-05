class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = list(range(len(nums)))
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, len(nums)):
            if dp[i-1] + nums[i] > nums[i]:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
            if dp[i] > res:
                res = dp[i]
        return res

    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if tmp + nums[i] > nums[i]:
                tmp = tmp + nums[i]
            else:
                tmp = nums[i]
            if tmp > res:
                res = tmp
