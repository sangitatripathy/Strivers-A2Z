class Solution:
    def subarrayXor(self, arr, k):
      # count=0
      # for i in range(len(arr)):
      #   xor=0
      #   for j in range(i,len(arr)):
      #     xor = xor ^ arr[j]
      #     if xor == k:
      #       count+=1
      # return count

      freq={}
      freq[0] = 1
      xor=0
      count=0
      for i in range(len(arr)):
        xor = xor ^ arr[i]
        if xor ^ k in freq:
          count+=freq[xor^k]
        freq[xor] = freq.get(xor,0)+1
      return count
        

sol = Solution()
arr= [4, 2, 2, 6, 4]
k = 6
print(sol.subarrayXor(arr,6))
            
            
          
        