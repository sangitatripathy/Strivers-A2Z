def minJumps(arr):
  max_ind=0
  for i in range (len(arr)):
      if i > max_ind :
          return False
      max_ind=max(max_ind,i+arr[i])
  return True 
    
arr= [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr))