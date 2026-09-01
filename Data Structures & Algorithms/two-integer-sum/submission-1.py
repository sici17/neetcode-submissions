class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map={}
        res=[None,None]

        for i in range(len(nums)):
            ret= map.get(target-nums[i])
            if(ret!=None and i!=ret ):
                res[0]=ret
                res[1]=i
                return res
            else:
                map[nums[i]]=i


