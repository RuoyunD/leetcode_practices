class Solution:
    def __init__(self):
        self.store = {}
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            dif = target - nums[i]
            if dif not in self.store:
                self.store[nums[i]] = i
            else:
                return [i, self.store[dif]]
