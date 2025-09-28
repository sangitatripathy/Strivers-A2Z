# Input: patterns = ["a","abc","bc","d"], word = "abc" Output: 3
class Solution(object):
    def numOfStrings(self, patterns, word):
      count=0
      for w in patterns:
        if word.find(w) != -1 :
          count+=1
      return count  

patterns = ["a","abc","bc","d"]
word = "abc"
s=Solution()
print(s.numOfStrings(patterns,word))    
         