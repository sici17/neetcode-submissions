class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        risultato=[]

        def backtrack(indice,percorso):

            risultato.append(list(percorso))

            for i in range(indice,len(nums)):

                percorso.append(nums[i])

                backtrack(i+1, percorso)

                percorso.pop()
            
        backtrack(0,[])
        return risultato
        