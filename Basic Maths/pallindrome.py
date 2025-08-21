def isPalindrome(n):
  if n == 0 :
      return True
  else:
      x=n
      rev=0
      while x > 0 :
          num=x%10
          rev=rev*10+num
          x=x//10
      if rev == n :
          return True
  return False
print(isPalindrome(555))