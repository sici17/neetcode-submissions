class Solution:
    def findMin(self, nums: List[int]) -> int:

        l=0
        r=len(nums)-1
        minimo=nums[0]

        while l<=r:

            mid=(r-l)//2+l
            minimo=min(nums[mid],minimo)

            if nums[l] <= nums[mid] and nums[r]<nums[l]:
                l=mid+1
            
            else:
                r=mid-1
            
        
        return minimo

        
        