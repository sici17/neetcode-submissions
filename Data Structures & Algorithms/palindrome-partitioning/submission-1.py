class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res=[]
        path=[]

        def dfs(start):

            if start==len(s):
                res.append(path.copy())
                return
            
            for end in range(start+1,len(s)+1):
                pezzo=s[start:end]
                if pezzo!=pezzo[::-1]:
                    continue
                path.append(pezzo)
                dfs(end)
                path.pop()
        
        dfs(0)
        return res
            

            


            
                
                
        