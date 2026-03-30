class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        answer = []

        print(path)
        
        for p in path:
            if p == '' or p == '.':
                continue

            if answer and p == '..':
                answer.pop()
                continue

            if not answer and p == '..':
                continue

            answer.append(p)

        return "/"+'/'.join(answer)

            