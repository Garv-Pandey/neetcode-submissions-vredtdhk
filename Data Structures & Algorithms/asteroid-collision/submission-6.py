class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        droid_counter = 0
        while droid_counter < len(asteroids):
            if not stack:
                stack.append(asteroids[droid_counter])
                droid_counter+=1
                continue

            # if stack is not empty

            # if they are moving in same direction
            if (stack[-1] < 0 and asteroids[droid_counter] < 0) or (stack[-1] > 0 and asteroids[droid_counter] > 0):
                stack.append(asteroids[droid_counter])
                droid_counter+=1
                continue

            # if they are moving in opposite direction
            
            # if left is negative and right is positive
            if (stack[-1] < 0 and asteroids[droid_counter]>0):
                stack.append(asteroids[droid_counter])
                droid_counter+=1
                continue

            # if left is moving right (positive) and right is moving left (negative):
            if stack[-1] < abs(asteroids[droid_counter]):
                stack.pop()
                continue

            if stack[-1] == abs(asteroids[droid_counter]):
                stack.pop()
                droid_counter+=1
                continue

            if stack[-1] > abs(asteroids[droid_counter]):
                droid_counter+=1
                continue

        return stack