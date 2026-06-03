class Solution:
  def findTwoElement(self, arr):
    freq=[0]*(len(arr)+1)
    for n in arr:
      freq[n]+=1
    repeat=-1
    miss=-1
    for i in range(1,len(arr)+1):
      if freq[i]== 0:
        miss=i
      if freq[i] == 2:
        repeat=i
    return [repeat,miss]
    
    


