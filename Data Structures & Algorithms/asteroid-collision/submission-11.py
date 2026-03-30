class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        i = 0
        while i < len(asteroids):
            if not stack:
                stack.append(asteroids[i])
                i+=1
                continue

            if (asteroids[i]<0 and stack[-1]<0) or (asteroids[i]>0 and stack[-1]>0) or (asteroids[i]>0 and stack[-1]<0):
                stack.append(asteroids[i])
                i+=1
                continue

            if abs(asteroids[i]) > abs(stack[-1]):
                stack.pop()
                continue

            
            if abs(asteroids[i]) == abs(stack[-1]):
                stack.pop()
                i+=1
                continue
            
            if abs(asteroids[i]) < abs(stack[-1]):
                i+=1
                continue

        return stack