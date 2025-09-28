def buySellStock(arr):
  # max_profit=0
  # for i in range (len(arr)):
  #   for j in range(0,i):
  #     if arr[i]-arr[j] > max_profit:
  #       max_profit=arr[i]-arr[j]
  # return max_profit
  min_el=arr[0] 
  max_profit=0
  for i in range(1,len(arr)):
    profit=arr[i]-min_el
    max_profit=max(max_profit,profit)
    min_el=min(min_el,arr[i])
  return max_profit
    

print(buySellStock([7,1,5,3,6,4]))
  