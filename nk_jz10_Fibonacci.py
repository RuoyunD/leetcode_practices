#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
class Solution:
  # 循环解法
    def Fibonacci(self , n: int) -> int:
        if n == 1 or n == 2:
            return 1
        res = 0
        pre = 1
        prePre = 1
        for i in range(3, n + 1):
            res = pre + prePre
            prePre = pre
            pre = res
        return res

    def __init__(self) -> None:
        self.store = {}
  #递归
    def Fibonacci(self , n: int) -> int:
        if n == 1 or n == 2:
            return 1
        if n not in self.store:
            self.store[n] = self.Fibonacci(n-1) + self.Fibonacci(n-2)
        return self.store[n]
