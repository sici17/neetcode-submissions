class Solution:
    def minWindow(self, s: str, t: str) -> str:

        map1, map2 = {}, {}

        have, j = 0, 0

        for i in range(len(t)):
            map1[t[i]]=map1.get(t[i],0)+1
        
        need=len(map1)
        min_lenght=len(s)
        flag=False

        
        for i in range(len(s)):
            
            if s[i] in map1:
                map2[s[i]]=map2.get(s[i],0)+1
                if map2[s[i]]==map1[s[i]]:
                    have+=1
            
            while have==need and j<=i:
                flag=True
                if i-j+1<=min_lenght:
                    min_lenght=i-j+1
                    index=i
                if s[j] in map1:
                    map2[s[j]]=map2.get(s[j],0)-1
                    if map2[s[j]]<map1[s[j]]:
                       have-=1
                j+=1
        
        if(flag):
            return s[index-min_lenght+1:index+1]

        return ""







        

                




        
        

                




            







        
        