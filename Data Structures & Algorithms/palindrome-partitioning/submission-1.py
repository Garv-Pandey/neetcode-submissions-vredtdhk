class Solution:
    def isPalindrome(self, string, start_index, end_index):
        i = start_index
        j = end_index

        while i<j:
            if string[i] != string[j]:
                return False
            
            i+=1
            j-=1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []
        subset = []


        def dfs(index):
            if index>=len(s):
                result.append(subset.copy())
            
            for i in range(index, len(s)):
                if self.isPalindrome(s, index, i):
                    subset.append(s[index:i+1])
                    dfs(i+1)
                    subset.pop()
        
        dfs(0)
        return result
