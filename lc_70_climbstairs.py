class Solution:
    # 直接使用递归
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        if n == 2:
            return 2
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        return res

    # 记忆化递归
    def __init__(self):
        self.store = {}

    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        if n == 2:
            return 2
        if n not in self.store:
            tmpRes = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.store[n] = tmpRes
            return tmpRes
        else:
            return self.store[n]

    # 循环解法
    def climbStairs(self, n):
        if n == 1: 
            return 1
        if n == 2:
            return 2
        pre = 2
        res = 0
        prePre = 1
        for i in range(3, n + 1):
            res = pre + prePre
            prePre = pre
            pre = res
            
        return res
