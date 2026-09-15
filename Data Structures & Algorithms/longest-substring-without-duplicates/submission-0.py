class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        j=0
        mappa={}
        massimo=0

        for i in range(len(s)):
            if s[i] in mappa and mappa[s[i]]>=j:
                j=mappa[s[i]]+1

            mappa[s[i]]=i
            if(i-j+1>massimo):
                massimo=i-j+1
    
        return massimo
       







        