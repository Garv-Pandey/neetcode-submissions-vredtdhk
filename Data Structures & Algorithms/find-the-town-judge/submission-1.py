class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        person_arr = [0] *n # index -> person_label, value = incoming trust - outgoing trust

        for i in range(len(trust)):
            trust_out, trust_in = trust[i]

            person_arr[trust_out - 1] -= 1
            person_arr[trust_in - 1] += 1
        

        for j in range(len(person_arr)):
            if person_arr[j] == n-1:
                return j+1
        
        return -1