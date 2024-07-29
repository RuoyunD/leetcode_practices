class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Last = m - 1
        fillPos = m + n - 1
        for i in range(n - 1, -1, -1):
            if m != 0 and nums1Last >= 0: 
                while nums2[i] < nums1[nums1Last]:
                    nums1[fillPos] = nums1[nums1Last]
                    nums1Last -= 1
                    fillPos -= 1
                    if nums1Last < 0: 
                        break
            
            nums1[fillPos] = nums2[i]
            fillPos -= 1
