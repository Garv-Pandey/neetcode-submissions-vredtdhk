class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        l, r= 0,0
        dictS = defaultdict(int)
        
        for r in range (len(s)):
            dictS[s[r]] += 1

            while (r-l+1) - max(dictS.values()) > k :
                dictS[s[l]] -= 1
                l +=1

            result = max(result, r-l+1)
            print(dictS)
            print(result)

        return result