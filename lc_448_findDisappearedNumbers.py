class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            if nums[i] > 0:
                if nums[nums[i]-1] > 0:
                    nums[nums[i]-1] = -nums[nums[i]-1]
            else:
                tmp = -(nums[i])
                if nums[tmp-1] > 0:
                    nums[tmp-1] *= -1

        res = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
