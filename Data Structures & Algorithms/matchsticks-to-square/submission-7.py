class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4 != 0:
            return False

        length = sum(matchsticks)//4
        sides = [0, 0, 0, 0]
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i == len(matchsticks):
                return sides[0] ==sides[1]==sides[2]==sides[3]
            
            for side_no in range(4):
                if sides[side_no] + matchsticks[i] <= length:
                    sides[side_no] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[side_no] -= matchsticks[i]
            
                if sides[side_no] == 0:
                    break

            return False
        
        return dfs(0)