class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        j=0
        mappa={}

        massimo=""
        massimeric=0

        ret=0

        for i in range(len(s)):

            mappa[s[i]]=mappa.get(s[i],0)+1

            if(mappa[s[i]]>massimeric):
                massimeric=mappa[s[i]]
                massimo=s[i]

            if(i-j+1>ret and k+massimeric>=i-j+1):
                ret=i-j+1
            else:
                mappa[s[j]]=mappa.get(s[j],0)-1
                j+=1
                

        return ret





        



        
            
        
        
        
            
            

            


                


            

        