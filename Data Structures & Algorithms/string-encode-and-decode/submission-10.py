class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f'{len(s)}#{s}'
                          
        return encoded

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            word_len = ''
            while s[i]!='#':
                word_len += s[i]
                i+=1
            
            answer.append(s[i+1: i+int(word_len)+1])
            i += int(word_len)+1

        return answer