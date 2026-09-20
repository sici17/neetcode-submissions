class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue=deque()
        ret=[]
        l=0

        for r in range(len(nums)):
            

            while queue and nums[r]>nums[queue[-1]]:
                queue.pop()
            
            queue.append(r)


            if r-l+1==k:
                ret.append(nums[queue[0]])
                l+=1
            
            if l>queue[0]:
                print(queue.popleft())
            
        return ret





        

            
            


        


            




        