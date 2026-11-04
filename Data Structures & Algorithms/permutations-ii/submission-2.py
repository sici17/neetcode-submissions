class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(indice):

            if indice == len(nums):
                res.append(list(nums))
                return
            
            visti=set()
            
            for i in range(indice,len(nums)):

                if nums[i] in visti:
                    continue
                visti.add(nums[i])
                
                nums[indice], nums[i] = nums[i], nums[indice]

                backtrack(indice+1)
            
                nums[indice], nums[i] = nums[i], nums[indice]
            

        nums.sort()    
        backtrack(0)
        return res
        