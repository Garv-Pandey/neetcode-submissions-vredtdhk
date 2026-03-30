class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_index = 0

        for i in range (len(strs[0])):
            for s in strs:
                if i >= len(s) or strs[0][i] != s[i]:
                    
                    if s[:i]=="":
                        return ""
                    return s[:i]
            
        
        return (strs[0])