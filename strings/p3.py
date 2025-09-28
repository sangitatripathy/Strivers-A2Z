class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        prefix=""
        for word in words:
            prefix+=word
            if prefix== s:
              return True 
            if len(prefix) > len(s):
              return False 
        return False     
      
s=Solution() 
words = ["i","love","leetcode","apples"]
print(s.isPrefixString("iloveleetcode",words) )      