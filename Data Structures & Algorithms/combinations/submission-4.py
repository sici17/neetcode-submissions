class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res=[]

        def backtrack(indice,percorso):

            if len(percorso)==k:
                res.append(list(percorso))
                return
            

            for i in range(indice,n+1):

                percorso.append(i)

                backtrack(i+1,percorso)

                percorso.pop()
            
        backtrack(1,[])
        return res

        
        