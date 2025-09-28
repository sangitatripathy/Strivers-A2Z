def sortColors(nums) -> None:
  mid=0
  low=0
  high=len(nums)-1
  while(mid <= high):
      if nums[mid] == 0 :
          temp=nums[low]
          nums[low]=nums[mid]
          nums[mid]=temp
          low+=1
          mid+=1
      elif nums[mid] == 1:
          mid+=1
      else:
          temp=nums[high]
          nums[high]=nums[mid]
          nums[mid]=temp
          high-=1
  print(nums)
        
sortColors([2,0,2,1,1,0])
    