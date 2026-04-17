class Solution:
    def count_NGE(self, arr, indices):
      res=[]
      for i in indices:
        count=0
        for j in range(i+1,len(arr)):
          if arr[j] > arr[i]:
              count+=1
        res.append(count)
      return res