class Solution:

    def rec(self, s: str, i: int, j: int) -> bool:
        while i<j:
            if(s[i]==s[j]):
                i+=1
                j-=1
            else:
                return False
        return True
         


    def validPalindrome(self, s: str) -> bool:

        i=0
        j=len(s)-1

        while i<j:
            if(s[i]==s[j]):
                i+=1
                j-=1
            else:
                return ( self.rec(s, i+1, j) or  self.rec(s, i, j-1))
        return True
        
        



        

        
        