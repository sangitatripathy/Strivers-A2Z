class Solution:
  def majorityElement(self, nums):
    # Brute
    # count=len(nums)//3
    # freq={}
    # res=[]
    # for i in nums:
    #     freq[i] = freq.get(i,0)+1
    #     if freq[i] > count and i not in res:
    #       res.append(i)
    # return res
    count1,count2=0,0
    el1,el2=0,0
    res=[]
    n=len(nums)
    for num in nums:
      if count1 == 0 and num != el2:
        count1+=1
        el1=num
      elif count2 == 0 and num != el1:
        count2+=1
        el2=num
      elif el1 == num:
        count1+=1
      elif el2 == num:
        count2+=1
      else:
        count1 -= 1
        count2 -= 1
        
    count1,count2 = 0,0
    
    for num in nums:
      if num == el1:
        count1+=1
      if num == el2:
        count2+=1

    if count1 > n//3:
      res.append(el1)
    if count2 > n//3:
      res.append(el2)
    return res

nums = [0,0,0]
sol= Solution()
print(sol.majorityElement(nums))      
            
        