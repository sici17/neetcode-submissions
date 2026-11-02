class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        risultato=[]
        candidates.sort()

        def backtrack(indice,percorso,somma):

            if somma==target:
                risultato.append(list(percorso))
                return
            
            if somma>target:
                return
            
            for i in range(indice,len(candidates)):
                
                if i>indice and candidates[i] == candidates[i-1]:
                    continue
                percorso.append(candidates[i])

                backtrack(i+1,percorso,somma+candidates[i])

                percorso.pop()

        backtrack(0,[],0)
        return risultato
        