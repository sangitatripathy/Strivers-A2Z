def rotateArray(arr,k,flag):
  d=k%len(arr)
  if flag == 'left':
    return arr[d:] + arr[:d]
  else:
    return arr[-d:]+arr[:-d]
    
print(rotateArray([41,67,27,26,69,72,8,2,64,96,8,78,19,48,60],2,'left'))
print(rotateArray([41,67,27,26,69,72,8,2,64,96,8,78,19,48,60],2,'right'))