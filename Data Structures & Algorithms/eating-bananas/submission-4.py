class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l=1
        r=max(piles)
        ret=r

        while l<=r:

            mid=(r+l)//2
            time=0

            for pile in piles:
                time+=(pile + mid - 1) // mid

            if time>h:
                l=mid+1
            else:
                r=mid-1
                ret=mid

            
        return ret
                






        
            


        
