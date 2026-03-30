class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_data = [] # gathering postion and speed of cars in a subarrays
        for i in range (len(speed)):
            car_data.append([position[i], speed[i]])
        
        car_data.sort(reverse=True) # car closest to target is at first index
        
        stack = list()
        for position, speed in car_data:
            time_to_reach = (target-position)/speed

            # if the time to reach target of a car is less than the car ahead of it, it will form a group with the car ahead of it.
            # we only push those cars which form a seperate group i.e., whose time to reach is > the car ahead of them (time_to_reach on top of stack)
            if len(stack) == 0 or time_to_reach > stack[-1]:
                stack.append(time_to_reach)

        return len(stack)
            