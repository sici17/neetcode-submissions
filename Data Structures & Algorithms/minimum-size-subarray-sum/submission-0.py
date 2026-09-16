class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        j=0
        ret=len(nums)+1
        somma=0

        for i in range(len(nums)):
            somma+=nums[i]
            while somma>=target and j<=i:
                if(i-j+1<=ret):
                    ret=i-j+1
                somma-=nums[j]
                j+=1
        
        if(ret==len(nums)+1):
            return 0
        else:
            return ret



        