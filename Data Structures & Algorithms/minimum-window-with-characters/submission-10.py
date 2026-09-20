class Solution:
    def minWindow(self, s: str, t: str) -> str:

        map1, map2 = {}, {}

        have, need = 0, 0

        for i in range(len(t)):
            map1[t[i]]=map1.get(t[i],0)+1
        
        need=len(map1)
        j=0
        min_lenght=len(s)
        ret=""
        
        for i in range(len(s)):
            
            if s[i] in map1:
                map2[s[i]]=map2.get(s[i],0)+1
                if map2[s[i]]==map1[s[i]]:
                    have+=1
            
            while have==need and j<=i:
                if i-j+1<=min_lenght:
                    min_lenght=i-j+1
                    ret=s[j:i+1]
                if s[j] in map1:
                    map2[s[j]]=map2.get(s[j],0)-1
                    if map2[s[j]]<map1[s[j]]:
                       have-=1
                j+=1
        return ret







        

                




        
        

                




            







        
        