class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        j=0
        h=set()

        for i in range(len(nums)):

            if(abs(i-j)>k):
                h.discard(nums[j])
                j+=1
                h.add(nums[j])
                
            if nums[i] in h and i!=j:
                return True
            else:
                h.add(nums[i])
                
        return False
            

       

           





                    

        