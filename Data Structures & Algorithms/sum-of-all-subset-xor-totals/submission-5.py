class Solution:
    somma=0
    def subsetXORSum(self, nums: List[int]) -> int:

        risultati=[]

        def backtrack(indice_partenza, percorso, somma_corrente):

            self.somma+=somma_corrente
        
            for i in range(indice_partenza, len(nums)):

                percorso.append(nums[i])


                backtrack(i+1,percorso,somma_corrente ^ nums[i])

                percorso.pop()
        
        backtrack(0,[],0)
        return self.somma


        
        