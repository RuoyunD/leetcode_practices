class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        xor = x ^ y

        while xor != 0:
            dist += 1
            xor &= xor - 1
        return dist
