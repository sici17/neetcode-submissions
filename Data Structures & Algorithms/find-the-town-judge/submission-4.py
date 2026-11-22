class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        person = defaultdict(int)
        judge=-1

        for src, dest in trust:

            person[src]-=1
            person[dest]+=1
        

        for i in range(n+1):
            if person[i]==n-1:
                judge=i
                break

        return judge   









        