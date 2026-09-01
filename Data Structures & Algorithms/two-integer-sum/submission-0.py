class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map={}
        res=[None,None]

        for i in range(len(nums)):
            map[nums[i]]=i
        
        for i in range(len(nums)):
            ret= map.get(target-nums[i])
            if(ret!=None and i!=ret ):
                res[0]=i
                res[1]=ret
                return res
                


