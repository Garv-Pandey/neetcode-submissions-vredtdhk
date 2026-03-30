class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        
        setS = set()

        l = 0
        r = 0
        for r in range(len(s)):
            
            while s[r] in setS:
                setS.remove(s[l])
                l += 1

            setS.add(s[r])
            result = max(result, r-l+1)

        return result