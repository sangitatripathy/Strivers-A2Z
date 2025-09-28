def evenlyDivides(n):
    num=n
    count=0
    while num>0:
        temp=num%10
        if temp!=0 and n%temp == 0:
            count+=1
        num=num//10
    return count   
print(evenlyDivides(12))