class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        risultato=[]

        def backtrack(indice,percorso,somma):

            if somma==target:
                risultato.append(list(percorso))
                return
            
            if somma>target:
                return
            
            for i in range(indice,len(nums)):

                percorso.append(nums[i])

                backtrack(i,percorso,somma+nums[i])

                percorso.pop()

        backtrack(0,[],0)
        return risultato


        