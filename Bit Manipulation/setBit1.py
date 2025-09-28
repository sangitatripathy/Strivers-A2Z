class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        for i in range(0,31):
            if n &(1<<i):
                count+=1
        return count

num=Solution()

print(num.hammingWeight(11))