class Solution:
  def isPalindrome(self, s):
    rev = s[::-1]
    if s== rev:
        return True
    return False
        
sol = Solution()
print(sol.isPalindrome("abba"))