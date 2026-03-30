class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        # if len(s) == 1:
        #     return 1
        
        setWin = set()

        l, r =0,0

        while r<len(s) and l<=r:
            if s[r] not in setWin:
                setWin.add(s[r])
                r+=1
                continue

            result = max(result, r-l)

            setWin.remove(s[l])
            l+=1

        result = max(result, r-l)
        return result