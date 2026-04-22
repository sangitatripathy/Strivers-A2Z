class Solution:
    def asteroidCollision(self, asteroids):
      stack=[]
      for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
          if stack[-1] < -a:
            stack.pop()
          elif stack[-1] == -a:
            stack.pop()
            break
          else:
            break
        else:
          stack.append(a)
      return stack