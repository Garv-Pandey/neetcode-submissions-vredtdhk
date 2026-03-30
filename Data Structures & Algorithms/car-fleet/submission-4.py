class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = [(target-location)/speed for location, speed in sorted(zip(position, speed), key= lambda x: x[0], reverse=True)]

        fleet_count = 1
        leader_time = time[0]
        for t in time:
            if t<=leader_time:
                continue

            fleet_count +=1
            leader_time = t
        return fleet_count