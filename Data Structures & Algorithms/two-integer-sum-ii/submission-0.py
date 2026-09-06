class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i=0
        j= len(numbers)-1

        while i<j:

            sum2=numbers[i]+numbers[j]
            if sum2>target:
                j-=1
            elif sum2<target:
                i+=1
            else:
                return [i+1,j+1]

        




           
            
            








        