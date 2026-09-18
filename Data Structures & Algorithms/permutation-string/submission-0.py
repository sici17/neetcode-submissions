class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        arr=[0]*26

        for i in range(len(s1)):
            arr[ord(s1[i])-ord("a")]+=1

        j=0
        arr2=[0]*26
        count=0

        for i in range(len(s2)):

            arr2[ord(s2[i])-ord("a")]+=1

            count+=1

            if(count==len(s1)):
                if(arr==arr2):
                    return True
                else:
                    arr2[ord(s2[j])-ord("a")]-=1
                    j+=1
                    count-=1
        
        return False



            







        
       


            
        



        