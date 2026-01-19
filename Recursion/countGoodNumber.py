class Solution:
    # def countGoodNumbers(self, n: int):
    #   primes={2,3,5,7}
    #   even={0,2,4,6,8}
    #   count=0
    #   for num in range(10**n):
    #     s=str(num).zfill(n)
    #     is_good=True
    #     for i in range (n):
    #       digit=int(s[i])
    #       if i%2 == 0:
    #         if digit not in even:
    #           is_good=False
    #           break
    #       else:
    #         if digit not in primes:
    #           is_good=False
    #           break
    #     if is_good:
    #       count+=1
    #   return count
    def countGoodNumbers(self, n: int):
      if n==0:
        return 1
      mod=(10**9)+7
      even=(n+1)//2
      odd=n//2
      return (pow(5,even,mod)*pow(4,odd,mod))% mod

sol=Solution()
print(sol.countGoodNumbers(50))