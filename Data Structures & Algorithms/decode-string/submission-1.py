class Solution:
    def decodeString(self, s: str) -> str:
        
        answer = []
        for string in s:
            if string == ']':
                substring = ''

                while answer and answer[-1] != '[':
                    substring = answer.pop() + substring

                answer.pop()

                multiplier = ''
                while answer and answer[-1].isdigit():
                    multiplier = answer.pop() + multiplier

                answer.append(int(multiplier)*substring)
            else:
                answer.append(string)

        return ''.join(answer)