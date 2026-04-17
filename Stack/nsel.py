class Solution:
  def nextSmallerEle(self, arr):
    nse=[]
    stack=[]
    for i in arr[::-1]:
      if not stack:
        nse.append(-1)
        stack.append(i)
      elif stack[-1] < i:
        nse.append(stack[-1])
        stack.append(i)
      else:
        found=-1
        while stack and stack[-1] >= i:
          stack.pop()
        if stack: nse.append(stack[-1])
        else: nse.append(-1)
        stack.append(i)
    return nse[::-1]

arr = [8,8,2,2,4,9,1,1,5,10]
sol = Solution()
print(sol.nextSmallerEle(arr))
