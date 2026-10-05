class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1

        while l<=r:

            mid=(r+l)//2
            print(nums[mid])

            if nums[mid]>=nums[l]:
                if target<nums[l] or target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            
            else:
                if target>nums[r] or target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            
            if target==nums[mid]:
                return mid

            
        
        return -1

        

        