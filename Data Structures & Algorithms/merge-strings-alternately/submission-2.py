class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        point_1 = point_2 = 0
        turn = 1

        while point_1< len(word1) and point_2< len(word2):
            if turn == 1:
                answer.append(word1[point_1])
                point_1+=1
                turn=2
                continue

            elif turn == 2:
                answer.append(word2[point_2])
                point_2+=1
                turn=1
                continue

        while point_1< len(word1):
            answer.append(word1[point_1])
            point_1+=1
            continue

        while point_2< len(word2):
            answer.append(word2[point_2])
            point_2+=1
            continue

        return ''.join(answer)