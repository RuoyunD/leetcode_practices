class Solution:
    # res[i & i-1] 移除最后一位1
    def countBits(self, n: int) -> List[int]:
        res = list(range(n+1))
        for i in range(1, n+1):
            res[i] = res[i & i-1] + 1
        return res

    # 奇偶性
    def countBits(self, n: int) -> List[int]:
        res = list(range(n+1))
        for i in range(1, n+1):
            # 奇数
            if i & 1 == 1:
                # 在前一位偶数情况下加一位
                res[i] = res[i-1] + 1
            else:
                # 偶数移位，减半
                res[i] = res[i>>1]
        return res
