class Solution:
    def trap(self, height):
      prefixMax=[0]*len(height)
      suffixMax=[0]* len(height)
      prefixMax[0] = height[0]
      suffixMax[-1] = height[-1]
      
      for i in range(1,len(height)):
        prefixMax[i]=max(prefixMax[i-1],height[i])

      for j in range(len(height)-2,-1,-1):
        suffixMax[j] = max(suffixMax[j+1], height[j])

      total=0
      for i in range(len(height)):
        total+=min(prefixMax[i],suffixMax[i])-height[i]
      return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol= Solution()
print(sol.trap(height))