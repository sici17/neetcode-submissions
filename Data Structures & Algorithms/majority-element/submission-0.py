class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        var=nums[0]
        count=1
        for i in range(1,len(nums)):
            if(count==0):
                var=nums[i]
            if(nums[i]==var):
                count+=1
            else:
                count-=1
        return var



            
        