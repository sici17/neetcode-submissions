class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        massimo, total = max(weights), sum(weights)
        res = total
        
        while massimo<=total:

            mid=(massimo+total)//2
            myday=1
            i=0
            curr=0

            while i<len(weights):
                if curr+weights[i]<=mid:
                    curr+=weights[i]
                else:
                    curr=weights[i]
                    myday+=1
                i+=1
  
            if myday>days:
                massimo=mid+1

            else:
                total=mid-1
                ret=mid

            
        return ret

        
        