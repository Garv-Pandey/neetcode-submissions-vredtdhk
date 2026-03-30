class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_stack = []

        path = path.split("/")
        print (path)

        for p in path:
            if path_stack and p =="..":
                path_stack.pop()
                continue

            if p == "." or p=="" or p == "..":
                continue

            path_stack.append(p)
            
        print(path_stack)

        return "/"+"/".join(path_stack)