class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        for i in range(0, len(nums)):
            while ptr < len(nums) and nums[ptr] == 0:
                ptr += 1
                
                
            if ptr > len(nums) - 1:
                    nums[i] = 0
            else:
                nums[i] = nums[ptr]
                ptr += 1
