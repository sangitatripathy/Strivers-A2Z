class Solution:
    def countWords(self, s: str) -> int:
      updatedword = s.replace("\n"," ").replace("\t"," ")
      res=updatedword.split()
      return len(res)

sol = Solution()
sol.countWords("a\nyo\t")

        