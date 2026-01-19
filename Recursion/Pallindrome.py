def isPalindrome(s):
  n=len(s)
  for i in range (n//2):
    if s[i] != s[n-i-1]:
      return False
  return True


def isPalindrome (s,ind):
  n=len(s)
  if ind >= n//2 :
    return True
  if s[ind] == s[n-ind-1] :
    return isPalindrome(s,ind+1)
  else:
    return False

s = "abba"
print(isPalindrome(s,0))


  
    
        