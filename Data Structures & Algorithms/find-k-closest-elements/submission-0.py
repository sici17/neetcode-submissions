class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        j=0
        skip=0

        for i in range(len(arr)-1):
            
            if i-j+1>=k:
                diffI=abs(arr[i+1]-x)
                diffJ=abs(arr[j]-x)
                if (diffI<diffJ):
                    j+=skip+1
                    skip=0
                elif(diffI==diffJ):
                    skip+=1

        
        return arr[j:j+k]













        