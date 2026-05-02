def fractionalKnapsack(val, wt, capacity):
  count=0
  ratio=[]
  for i in range(len(val)):
    ratio.append((val[i],wt[i],val[i]/wt[i]))
  ratio.sort(key=lambda x:x[2], reverse=True)
  for value,weight,r in ratio:
    if capacity >= weight:
      count+=value
      capacity-=weight
    else:
      count+= (value *(capacity/weight))
  return count
val= [60, 100, 120]
wt= [10, 20, 30]
print(fractionalKnapsack(val,wt,50))
    