class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l=0
        r=len(nums)-1

        while l<=r:

            mid=(r+l)//2

            if nums[mid]>nums[l]:
                if target<nums[l] or target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            
            elif nums[mid]==nums[l]:
                l+=1 
            else:
                if target>nums[r] or target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            
            if target==nums[mid]:
                return True

            
        
        return False
        