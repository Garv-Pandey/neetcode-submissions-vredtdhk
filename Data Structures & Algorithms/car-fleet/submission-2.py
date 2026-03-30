class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        reachTime = [ (target-pos)/speed for pos,speed in sorted(zip(position, speed), key = lambda x: x[0], reverse=True)]
        print(reachTime)

        fleets = 0
        high_reachTime = 0
        for i in range(len(reachTime)):
            print(i, high_reachTime)
            if i > 0 and reachTime[i] <= high_reachTime:
                continue

            high_reachTime = reachTime[i]
            fleets+=1

        return fleets
