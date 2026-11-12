class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-s for s in nums]
        heapq.heapify(nums)

        while k>1:
            heapq.heappop(nums)
            k-=1
        
        return abs(nums[0]) if nums[0]<0 else -nums[0]

        
        