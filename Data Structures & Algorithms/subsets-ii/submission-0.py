class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res=[]

        nums.sort()

        def backtrack(indice,percorso):

            res.append(list(percorso))

            for i in range(indice,len(nums)):

                if i>indice and nums[i] == nums[i-1]:
                    continue

                percorso.append(nums[i])

                backtrack(i+1,percorso)

                percorso.pop()
            
        backtrack(0,[])
        return res
        