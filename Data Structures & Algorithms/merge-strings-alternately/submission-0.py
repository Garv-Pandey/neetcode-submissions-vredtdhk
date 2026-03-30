class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        
        point1, point2 = 0, 0

        turn = 1
        while point1<len(word1) and point2<len(word2):
            if turn == 1:
                answer += word1[point1]
                point1+=1
                turn = 2
            else: 
                answer += word2[point2]
                point2+=1
                turn = 1

        while point1<len(word1):
            answer+=word1[point1]
            point1+=1
        
        while point2<len(word2):
            answer+=word2[point2]
            point2+=1

        return answer
