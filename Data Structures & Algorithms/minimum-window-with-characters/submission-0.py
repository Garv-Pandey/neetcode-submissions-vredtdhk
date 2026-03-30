class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        result = ""
        dictT = dict()
        dictWindow = dict()

        for char in t:
            dictT[char] = dictT.get(char, 0) + 1
            dictWindow[char] = 0

        print(dictT)
        print(dictWindow)

        l,r =0,0
        if s[r] in dictT:
            dictWindow[s[r]]  +=1

        while l<=r and r< len(s):
            substring_valid = True

            # checking validity of substring
            for char, freq in dictT.items():
                if dictWindow[char] < freq :
                    substring_valid = False
                    break

            if substring_valid == True:
                if result == "" or len(result) > r-l+1:
                    result = s[l:r+1]  
                
                if s[l] in dictT:
                    dictWindow[s[l]] -= 1 
                l+=1
            else:
                r+=1
                if r<len(s) and s[r] in dictT:
                    dictWindow[s[r]] += 1

        return result
