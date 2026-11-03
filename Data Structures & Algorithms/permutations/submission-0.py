class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res=[]

        def backtrack(indice, percorso):

            if len(percorso)== len(nums):
                res.append(list(percorso))
                return
            
            for i in range(indice,len(nums)):

                if nums[i] in percorso:
                    continue

                percorso.append(nums[i])

                backtrack(indice,percorso)

                percorso.pop()

        backtrack(0,[])
        return res
        