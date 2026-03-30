class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result_indices = [-1,-1]
        result_len = float('inf')
        map_t = defaultdict(int)
        for char in t:
            map_t[char]+=1

        map_window = defaultdict(int)
        l=0
        for r in range(len(s)):
            # making hash map for window
            map_window[s[r]] +=1

            # checkind validity of window
            valid = True
            for key, value in map_t.items():
                if map_window[key]<value:
                    valid = False
                    break

            # when window is valid
            while valid :
                # updating the result if the window size is smaller
                if result_len > (r-l+1):
                    result_indices = [l,r]
                    result_len = r-l+1

                # increaementing left pointer and updating hash map and validity
                map_window[s[l]] -= 1
                l+=1

                for key, value in map_t.items():
                    if map_window[key]<value:
                        valid = False
                        break

        print (result_len)
        print (result_indices)

        if result_indices == [-1,-1]:
            return ""
        
        return s[result_indices[0]: result_indices[1]+1]