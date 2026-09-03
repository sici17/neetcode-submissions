class Solution:

    def encode(self, strs: List[str]) -> str:


        risultato = "".join(f"{len(s)}{'#'}{s}" for s in strs)


        return risultato




    def decode(self, s: str) -> List[str]:

        ret=[]
        lisnumero=[]
        i=0

        while i<len(s):


            if s[i]=='#':
                stringanum="".join(lisnumero)
                numero=int(stringanum)
                ret.append(s[i+1:numero+i+1])
                i+=numero+1
                lisnumero=[]
                
            else:
                lisnumero.append(s[i])
                i+=1
        
        return ret




        

