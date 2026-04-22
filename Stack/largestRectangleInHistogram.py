class Solution:
    def largestRectangleArea(self, heights):
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


sol = Solution()
heights = [2,1,5,6,2,3]
print(sol.largestRectangleArea(heights))
          
      