class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        r = 0
        l = 0

        dictS = defaultdict(int)
        for r in range(len(s)):
            dictS[s[r]] += 1
            print(dictS)

            if (r-l+1) - max(dictS.values()) <= k:
                result = max(result, r-l+1)
                print(f' updated {result}')
                continue

            dictS[s[l]] -=1
            l+=1

        result = max(result, r-l+1)
        return result