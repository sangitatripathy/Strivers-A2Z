class Solution:
    def maximalRectangle(self, matrix):
      def largestRectangleArea(heights):
        n = len(heights)
        nse=[0]*n
        pse=[0]*n
        stack=[]
        for i in range (n-1,-1,-1):
          while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
          if not stack:
            nse[i] = n
          else:
            nse[i] = stack[-1]
          stack.append(i)
        stack=[]
        for i in range(n):
          while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
          if not stack:
            pse[i] = -1
          else:
            pse[i] = stack[-1]
          stack.append(i)
        maxarea= 0
        for i in range(n):
          width = nse[i] - pse[i] -1
          height = heights[i]
          maxarea= max(maxarea, width*height)
        return maxarea
      n= len(matrix)
      m = len(matrix[0])
      psum= [[0]*m for _ in range(n)]
      for j in range(m):
        s=0
        for i in range(n):
          if int(matrix[i][j]) == 0:
            s=0
          s= s + int(matrix[i][j])     
          psum[i][j] =s
      maxarea=0
      for i in range(n):
        maxi = largestRectangleArea(psum[i])
        maxarea =max(maxarea,maxi)
      return maxarea
          

sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(sol.maximalRectangle(matrix))