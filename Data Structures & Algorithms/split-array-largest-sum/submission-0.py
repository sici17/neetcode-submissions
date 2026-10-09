class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def cansplit(mid):
            subs=1
            somma=0
            for num in nums:
                somma+=num
                if somma>mid:
                    subs+=1
                    if subs>k:
                        return False
                    somma=num
            return True




        l=max(nums)
        r=sum(nums)
        ret=0

        while l<=r:

            mid= (l+r)//2

            if cansplit(mid):
                ret=mid
                r=mid-1
            else:
                l=mid+1
        return ret


        




        