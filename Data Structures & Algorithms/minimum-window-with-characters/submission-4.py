class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        
        dict_t = defaultdict(int)
        for char in t:
            dict_t[char]+=1

        dict_s = defaultdict(int)
        for i in range(len(t)):
            dict_s[s[i]]+=1

        match_score = 0
        for key, value in dict_t.items():
            if dict_s[key] >= value:
                match_score+=1

        if match_score == len(dict_t):
            return s[0: len(t)]
 
        l = 0
        min_indices = [0, float('inf')]
        for r in range(len(t), len(s)):
            print(s[l:r+1])
            dict_s[s[r]]+=1

            if s[r] in dict_t and dict_s[s[r]] == dict_t[s[r]]:
                match_score+=1

            while match_score == len(dict_t):
                if min_indices[1]-min_indices[0]+1 > r-l+1:
                    min_indices[0] = l
                    min_indices[1] = r

                if s[l] in dict_t and dict_s[s[l]] == dict_t[s[l]]:
                    match_score -= 1
                
                dict_s[s[l]] -= 1
                l+= 1

        if min_indices[1]==float('inf'):
            return ""

        return s[min_indices[0]: min_indices[1]+1]