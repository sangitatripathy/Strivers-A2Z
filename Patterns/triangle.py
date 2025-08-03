class Solution:
    def printTriangle(self, N):
        for i in range (N):
            for k in range (N-i-1):
                print(" ",end="")
            for j in range (i*2+1):
                print("*",end="")
            print()

num=Solution()
num.printTriangle(5)