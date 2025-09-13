def numAppearsOnce(arr):
  freq={}
  for num in arr:
    freq[num]=freq.get(num,0)+1
  for num in freq:
    if freq[num] == 1:
      return num