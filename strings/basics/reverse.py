class Solution:
    def reverseWords(self, s: str) -> str:
     str= s.split()
     revstr= str[::-1]
     print(" ".join(revstr))

sol= Solution()
sol.reverseWords("the sky is blue")