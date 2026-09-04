class Solution:
    def isPalindrome(self, s: str) -> bool:

      j=len(s)-1
      i=0

      while i<(len(s)//2):
        if(not s[i].isalnum()):
          i+=1
        elif(not s[j].isalnum()):
          print("hey")
          j-=1
        else:
          if(s[i].casefold()!=s[j].casefold()):
            return False
          else:
            i+=1
            j-=1
        
      return True
        


            
        