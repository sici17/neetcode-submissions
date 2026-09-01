class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map={}

        for i in range(len(nums)):
            ret= map.get(target-nums[i])
            if(ret!=None and i!=ret ):
                return [ret,i]
            else:
                map[nums[i]]=i


