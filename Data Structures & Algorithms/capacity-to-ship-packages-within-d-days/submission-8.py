class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        massimo, total = max(weights), sum(weights)
        res = total
        
        while massimo<=total:

            mid=(massimo+total)//2
            myday=1
            curr=0

            for weight in weights:
                if curr+weight<=mid:
                    curr+=weight
                else:
                    curr=weight
                    myday+=1
  
            if myday>days:
                massimo=mid+1

            else:
                total=mid-1
                ret=mid

            
        return ret

        
        