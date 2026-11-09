class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total=sum(nums)
        if total%k!=0:
            return False

        target=total//k
        sums=[0]*k

        def dfs(i):

            if i==len(nums):
                return True

            posizione = nums[i]
            tried_sums=set()

            for group in range(k):
                curr=sums[group]
                if curr+posizione>target or curr in tried_sums :
                    continue

                tried_sums.add(curr)
                sums[group]+=posizione
                found=dfs(i+1)
                sums[group]-=posizione

                if found:
                    return True

            return False

        return dfs(0)
        