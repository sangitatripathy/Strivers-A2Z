# sum of digits of string after convert
# s = "iiii", k = 1  Output: 36
# Input: s = "leetcode", k = 2 Output: 6
class Solution(object):
    def getLucky(self, s, k):
      digit_str="".join(str(ord(char)-96) for char in s)
      while(k>0):
        sum_digits=sum(int(char) for char in digit_str)
        digit_str=str(sum_digits)
        k-=1
      return sum_digits 

s=Solution()
print(s. getLucky("leetcode",2))   


      